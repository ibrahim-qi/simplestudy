from flask import Flask, render_template, Blueprint, redirect, url_for, abort, flash, request
from flask_login import login_required, current_user
from app.forms import SetForm, FlashcardForm, EditFlashcardForm
from app.models.sets import Set
from app.models.flashcards import Flashcard
from app.models.selftests import SelfTest
from app.models.multiplechoicetests import MultipleChoiceTest
from app.models.multiplechoicequestions import Question, Option, Choice
from app.models.ratings import Rating

# creates the main blueprint
main = Blueprint('main', __name__)

# if there is no given route, it automatically redirects the user to the dashboard if they are logged in
@main.route('/')
@login_required
def index():
    return redirect(url_for('main.dashboard'))

# dashboard route
@main.route('/dashboard')
@login_required
def dashboard():
    # if current user is logged in
    if current_user.is_authenticated:
        sets = current_user.sets.all()  # assign all the sets created by the user to the sets variable
    else:
        sets = []
    return render_template('dashboard.html', sets=sets)

# browse page
@main.route('/browse')
@login_required
def browse():
    sets = Set.query.all()
    search = request.args.get('search')

    if search:
        sets = Set.query.filter(Set.setname.contains(search))
    else:
        sets = Set.query.all()
    return render_template('browse.html', sets=sets)

# search bar within the browse page
@main.route('/browse/search')
def search():
    # gets the text inputted into the search bar and assigns it to the search variable
    search = request.args.get('search')

    if search:
        # if the set name contains any of the text in the search, query the set
        sets = Set.query.filter(Set.setname.contains(search))
    else:
        # queries all sets
        sets = Set.query.all()
    return render_template('')

# creating a set
@main.route('/create-set', methods=['GET', 'POST'])
@login_required
def create_set():
    from app import db
    form = SetForm()
    if form.validate_on_submit():
        set_data = Set(setname=form.setname.data, # inputted set name in the form
                       user_id=current_user.id, # user id of the current user logged in
                       topic=form.topic.data, # topic name
                       subject=form.subject.data, # subject name
                       username=current_user.username,
                       ratingNo=5.00) # username of the current user logged in
        set.username = current_user.username
        db.session.add(set_data) # adds set to the database
        db.session.commit()
        return redirect(url_for('main.dashboard')) # redirects to the dashboard after set is creasted

    return render_template('create_set.html', form=form)

# set page
@main.route('/set/<int:id>') # route for the set of the set id
@login_required
def set(id):
    # query set id
    set = Set.query.get_or_404(id)
    # query rating for user id and current set
    rating = Rating.query.filter_by(user_id=current_user.id,setid=set.id).first()
    # if a rating does not exist for that user and set, the user has not rated yet
    if rating is None:
        hasRated = False
    else:
        hasRated = True
    return render_template('set.html', set=set, hasRated=hasRated)

# rating
@main.route('/set/<int:id>', methods=['GET', 'POST'])
@login_required
def rating(id):
    import statistics
    from app import db
    set = Set.query.get_or_404(id)
    # Convert String to Float
    ratingNumber = float(request.form.get('rating'))
    ratingList = []
    ratingList.append(set.ratingNo)
    ratingList.append(ratingNumber)
    print(ratingList)
    # Get average of the rating the user has given and the set's current rating
    newRating = statistics.mean(ratingList)
    rating = Rating(user_id=current_user.id,
                    setid=set.id,
                    ratingNo=ratingNumber,
                    hasRated=True)
    db.session.add(rating)
    db.session.commit()

    # Update Set Rating
    set.ratingNo = newRating
    db.session.commit()
    return redirect(url_for('.set', id=set.id))

# delete set
@main.route('/set/<int:id>/delete')
@login_required
def delete_set(id):
    from app import db
    set = Set.query.get_or_404(id)
    db.session.delete(set) # deletes queried set from the database
    db.session.commit()
    flash('Set {0} has been deleted'.format(set.setname)) # message display that set has been deleted to the user
    return redirect(url_for('main.dashboard'))

# flashcard page
@main.route('/set/<int:setid>/flashcard/<int:cardid>') # route for the flashcard in the set
@login_required
def flashcard(setid, cardid):
    set = Set.query.get_or_404(setid)
    flashcard = set.flashcards.filter_by(id=cardid).first() # query flashcard from the set
    if flashcard is None:
        abort(404) # redirects to error page
    return render_template('flashcard.html', set=set, flashcard=flashcard)

# add a flashcard to set
@main.route('/set/<int:id>/add-flashcards', methods=['GET', 'POST'])
@login_required
def add_flashcards(id):
    from app import db
    form = FlashcardForm()
    set = Set.query.get_or_404(id)
    if form.validate_on_submit():
        card = Flashcard(front=form.front.data, # front of the flashcard form data
                         back=form.back.data) # back of the flashcard form data
        set.flashcards.append(card) # adds flashcard to set list
        db.session.add(set) # adds set to database
        db.session.commit()
        # if user chooses to add another flashcard to set
        if form.next.data:
            return redirect(url_for('.add_flashcards', id=set.id))
        else:
            flash('Flashcard added to {0}'.format(set.setname))
            return redirect(url_for('.set', id=set.id))
    return render_template('add_flashcards.html', form=form, setname=set.setname)

# edit flashcard
@main.route('/set/<int:setid>/flashcard/<int:cardid>/edit', methods=['GET', 'POST'])
@login_required
def edit_flashcard(setid, cardid):
    from app import db
    form = EditFlashcardForm()
    set = Set.query.get_or_404(setid)
    flashcard = set.flashcards.filter_by(id=cardid).first()
    if flashcard is None:
        abort(404)
    if form.validate_on_submit():
        flashcard.front = form.front.data # assigns new front data to variable
        flashcard.back = form.back.data # assigns new back data to variable
        db.session.add(flashcard) # updates flashcard in database
        db.session.commit()
        flash('Flashcard was updated.')
        return redirect(url_for('.flashcard', setid=setid, cardid=cardid))
    form.front.data = flashcard.front
    form.back.data = flashcard.back
    return render_template('edit_flashcard.html', form=form, flashcard=flashcard, set=set)

# delete flashcard
@main.route('/set/<int:setid>/delete-flashcard/<int:cardid>')
@login_required
def delete_card(setid, cardid):
    from app import db
    flashcard = Flashcard.query.get_or_404(cardid)
    db.session.delete(flashcard) # delete flashcard from set
    db.session.commit()
    return redirect(url_for('.set', id=setid)) # redirect back to set

# starts self quiz and adds the data for the quiz to the database
@main.route('/set/<int:setid>/selfquiz/start', methods=['POST', 'GET'])
@login_required
def start_selfquiz(setid):
    from app import db
    set = Set.query.get_or_404(setid)
    totalFlashcards = set.flashcards.count() # counts number of flashcards in set
    flashcards = set.flashcards.filter().all() # query all flashcards in set

    if totalFlashcards >= 1: # self quiz cannot be taken if there is 0 flashcards in set
        # quiz data
        quiz = SelfTest(setid=set.id, # set id
                        user_id=current_user.id, # user id
                        rightCount=0, # number of flashcards the user has got correct
                        wrongCount=0, # number of flashcards the user has got incrorect
                        flashcardsCompleted=0, # number of flashcards completed so far in the quiz
                        frontNumber=0, # pointer for front side of flashcard in list
                        backNumber=0, # pointer for back side of flashcard in list
                        totalFlashcards=totalFlashcards)
        db.session.add(quiz)
        db.session.commit()
    else:
        return render_template('quizError.html', set=set) # if flashcards in set is 0, it will return error page

    return redirect(url_for('.self_quiz', setid=set.id, quizid=quiz.id))


# self quiz
@main.route('/set/<int:setid>/selfquiz/<int:quizid>', methods=['POST', 'GET'])
@login_required
def self_quiz(setid, quizid):
    flashcardFronts = [] # stores front of flashcards in set
    flashcardBacks = [] # stores back of flashcards in set
    set = Set.query.get_or_404(setid)
    quiz = SelfTest.query.get_or_404(quizid) # queries the quiz
    flashcards = set.flashcards.filter().all()

    # appends the front and back side for each flashcard in the set to the lists
    for flashcard in flashcards:
        flashcardFronts.append(flashcard.front)
        flashcardBacks.append(flashcard.back)

    # quiz.frontNumber & quiz.backNumber is used as an index position for the list
    return render_template('self_quiz.html', set=set, quiz=quiz, totalFlashcards=quiz.totalFlashcards,
                           flashcardFront=flashcardFronts[quiz.frontNumber], flashcardBack=flashcardBacks[quiz.backNumber],
                           rightCount=quiz.rightCount, wrongCount=quiz.wrongCount, flashcardsCompleted=quiz.flashcardsCompleted)

# if user gets question right
@main.route('/set/<int:setid>/selfquiz/<int:quizid>/right', methods=['POST', 'GET'])
@login_required
def right(setid, quizid):
    from app import db
    flashcardFronts = []
    flashcardBacks = []
    set = Set.query.get_or_404(setid)
    quiz = SelfTest.query.get_or_404(quizid)
    flashcards = set.flashcards.filter().all()
    for flashcard in flashcards:
        flashcardFronts.append(flashcard.front)
        flashcardBacks.append(flashcard.back)

    # checks to see if frontNumber is less than the length of list
    if quiz.frontNumber < len(flashcardFronts)-1:
        quiz.rightCount += 1 # increments right count
        quiz.flashcardsCompleted += 1 # increments flashcards completed
        quiz.frontNumber += 1 # increments frontNumber
        quiz.backNumber += 1 # increments backNumber
        db.session.add(quiz) # updates quiz in database
        db.session.commit()
        return redirect(url_for('.self_quiz', setid=set.id, quizid=quiz.id)) # redirects back to quiz
    # if last flashcard is chosen to be right
    else:
        quiz.rightCount += 1
        db.session.add(quiz)
        db.session.commit()
        # ends quiz and displays quiz results
        return redirect(url_for('.selfQuizResults', setid=set.id, quizid=quiz.id))

# if user gets question wrong
@main.route('/set/<int:setid>/selfquiz/<int:quizid>/wrong', methods=['POST', 'GET'])
@login_required
def wrong(setid, quizid):
    from app import db
    flashcardFronts = []
    flashcardBacks = []
    set = Set.query.get_or_404(setid)
    quiz = SelfTest.query.get_or_404(quizid)
    flashcards = set.flashcards.filter().all()
    for flashcard in flashcards:
        flashcardFronts.append(flashcard.front)
        flashcardBacks.append(flashcard.back)
    if quiz.frontNumber < len(flashcardFronts)-1:
        quiz.wrongCount += 1 # increments wrong count
        quiz.flashcardsCompleted += 1
        quiz.frontNumber += 1
        quiz.backNumber += 1
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('.self_quiz', setid=set.id, quizid=quiz.id))
    else:
        quiz.wrongCount += 1
        db.session.add(quiz)
        db.session.commit()
        return redirect(url_for('.selfQuizResults', setid=set.id, quizid=quiz.id))

# self quiz results
@main.route('/set/<int:setid>/selfquiz/<int:quizid>/results', methods=['POST', 'GET'])
@login_required
def selfQuizResults(setid, quizid):
    set = Set.query.get_or_404(setid)
    quiz = SelfTest.query.get_or_404(quizid)
    # calculates the percentage score for the quiz
    quiz.percentageScore = (quiz.rightCount/quiz.totalFlashcards)*100
    return render_template('selfQuizResults.html', set=set, rightCount=quiz.rightCount, wrongCount=quiz.wrongCount,
                           percentageScore=quiz.percentageScore)

@main.route('/set/<int:setid>/mcq/start', methods=['POST', 'GET'])
@login_required
def start_mcq(setid):
    import random
    from app import db
    set = Set.query.get_or_404(setid)
    flashcards = set.flashcards.filter().all()
    totalFlashcards = set.flashcards.count()

    if totalFlashcards >= 3:
        # Adds multiple choice test to the database
        quiz = MultipleChoiceTest(setid=set.id,
                                user_id=current_user.id,
                                score=0,
                                questionNumber=-1)
        db.session.add(quiz)
        db.session.commit()

        testChoices = []
        for flashcard in flashcards: # Iterates each flashcard in the set
            testChoices.append(flashcard.back) # Adds each of the back side of the flashcards to the list

        # Adds each question to the database
        for flashcard in flashcards:
            question = Question(testID=quiz.id,
                                question=flashcard.front,
                                flashcardid=flashcard.id,
                                answer=flashcard.back)

            db.session.add(question)
            db.session.commit()


        questions = quiz.questions.filter().all()

        # Adds random options
        for question in questions:
            for option in range(3):
                option = Option(question_id=question.id,
                                name=random.choice(testChoices))
                db.session.add(option)
                db.session.commit()

        # Adds the choices which will be displayed in the question
        for question in questions:
            choices = []
            options = question.options
            for option in options:
                choices.append(option.name)
            choices.append(question.answer)
            random.shuffle(choices) # Shuffles choices
            for i in range(4):
                question_choice = Choice(question_id=question.id,
                                         name=choices.pop())
                db.session.add(question_choice)
                db.session.commit()
    else:
        return render_template('quizError.html', set=set)

    return redirect(url_for('.multipleChoiceQuiz', setid=set.id, quizid=quiz.id))

@main.route('/set/<int:setid>/mcq/<int:quizid>', methods=['POST', 'GET'])
@login_required
def multipleChoiceQuiz(setid, quizid):
    import random
    from app import db

    # Holds questions for current quiz
    quizQuestions = []
    set = Set.query.get_or_404(setid)
    quiz = MultipleChoiceTest.query.get_or_404(quizid)
    questions = quiz.questions.filter().all()
    flashcards = set.flashcards.filter().all()

    # Adds each question to the list
    for question in questions:
        quizQuestions.append(question)

    # Uses flask request to receive which button the user has chosen and stores the value in user_answer
    user_answer = request.form.get('useranswer')
    question = quizQuestions[quiz.questionNumber] # Current question is the index of questionNumber in quizQuestions
    question.answer = question.answer.replace(" ", "") # Removes the spaces from the question answer
    # Checks if the current question is not the last question
    if quiz.questionNumber < len(quizQuestions)-1:
        # Increment score and question number
        if user_answer == question.answer:
                quiz.score += 1
                quiz.questionNumber += 1
                db.session.commit()
        if user_answer != question.answer:
                quiz.questionNumber += 1
                db.session.commit()
        # If it is the last question then display results after it is answered
    elif quiz.questionNumber == len(quizQuestions)-1:
        if user_answer == question.answer:
            quiz.score += 1
            db.session.commit()
            return redirect(url_for('.multipleChoiceResults', setid=set.id, quizid=quiz.id))
        if user_answer != question.answer:
            return redirect(url_for('.multipleChoiceResults', setid=set.id, quizid=quiz.id))



    return render_template('multipleChoiceQuiz.html', set=set, quiz=quiz, question=quizQuestions[quiz.questionNumber])

@main.route('/set/<int:setid>/mcq/<int:quizid>/results', methods=['POST', 'GET'])
@login_required
def multipleChoiceResults(setid, quizid):
    set = Set.query.get_or_404(setid)
    quiz = MultipleChoiceTest.query.get_or_404(quizid)
    percentageScore = (quiz.score/set.flashcards.count())*100
    wrongCount = set.flashcards.count() - quiz.score

    return render_template('multipleChoiceResults.html', set=set, quiz=quiz, percentageScore=percentageScore,
                           wrongCount=wrongCount)

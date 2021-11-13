init python:
    stats_unlocked = False
    todo_unlocked = False

    study_session_questions = general_questions

    has_visited_hacker_space_with_annika = False

    # once this is True, trivia guy no longer appears, and player can get a first round interview w/ CupCakeCPU
    has_won_hacker_space_trivia = False

    # player_stats.player_stats_map['CS Knowledge'] >= 80
    has_completed_curriculum = False

    day_activity = None # set in day_activity_choice.rpy

    topics_to_ask = set() # empty set

    ## TODO #################

    # TODO: refactor
    has_met_marco = False

    # TODO: definitely refactor
    interview_company_name = None
    days_before_interview = None

    offer_company_name = None
    days_before_offer = None

    has_received_offer = False
    # TODO: beyond demo version, can do negotiation
    has_accepted_offer = False

    # TODO: more day counters, more refactoring
    day_completed_curriculum = None
    # day counter of the first offer, subtract this from the other day counters
    day_of_first_offer = None

    seen_hacker_space_events = set()
    #################################

    ## Non-mutable

    # to-do strings
    todo_check_fcc = 'Check out [freeCodeCamp]'
    todo_ask_hackathon = 'Ask Annika about hackathons'
    todo_ask_curriculum = 'Ask Annika about CS curriculum'
    todo_learn_cs = 'Ramp up CS knowledge'
    todo_apply_cupcakecpu = 'Apply to CupcakeCPU'
    todo_apply_to_jobs = 'Apply to jobs'
    todo_interview_prep = 'Prepare for coding interviews'
    todo_ask = 'Learn about ' # should be concatenated with vocabs from barista story

    # story labels for hacker space and barista
    hacker_space_event_labels = [
    'hacker_space_tech_talk',
    'hacker_space_playtest',
    'hacker_space_project',
    'hacker_space_open_source',
    ]

    barista_event_labels = [
    'barista_fullstack'
    'barista_devops',
    'barista_conference',
    'barista_versioncontrol'

    'barista_machinelearning',
    'barista_agile',
    'barista_api',
    'barista_userexperience',
    
    ]

    ask_annika = {
    'Hackathon': label_ask_annika_hackathon,
    'Full-Stack': label_ask_annika_fullstack,
    'DevOps': label_ask_annika_devops,
    'Conference': label_ask_annika_conference,
    'Version Control': label_ask_annika_versioncontrol,
    }

    ask_marco = {
    'Machine Learning': label_ask_marco_machinelearning,
    'Agile': label_ask_marco_agile,
    'API': label_ask_marco_api,
    'User Experience': label_ask_marco_userexperience
    }
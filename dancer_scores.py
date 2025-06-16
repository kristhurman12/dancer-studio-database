def dancer_scores():
    competition_name = input("Enter the name of the competition: ")
    competition_date = input("Date (YYYY-MM-DD): ")

    try:
        technical_score = float(input("Enter the technical score (0-25): "))
        performance_score = float(input("Enter the performance score (0-25): "))
        choreography_score = float(input("Enter the choreography difficulty score (0-25): "))
        musicality_score = float(input("Enter the musicality score (0-25): "))
    except ValueError:
        print("Error. Please enter valid numbers for scores.")
        return None
    
    overall_score = (technical_score + performance_score + choreography_score + musicality_score)

    print("\nDancer Scores:")
    print("Competition:", competition_name)
    print("Date:", competition_date)
    print("Technical score:", technical_score)
    print("Performance score:", performance_score)
    print("Choreography score:", choreography_score)
    print("Musicality score:", musicality_score)
    print("Overall score:", overall_score)

    return {
        "competition": competition_name,
        "date": competition_date,
        "technical score": technical_score,
        "performance score": performance_score,
        "choreography score": choreography_score,
        "musicality score": musicality_score,
        "overall score": overall_score
    }

scores = dancer_scores()
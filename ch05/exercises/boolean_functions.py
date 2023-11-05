def percentage_to_letter(score = 0):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
def is_passing(letter = None):
    return letter in["A", "B", "C"]

def main():
    score = float(input("Enter your percentage grade: "))
    if 0 <= score <= 100:
        lettered_grade = percentage_to_letter(score)
        passing_grade = is_passing(lettered_grade)
        print("Your letter grade is ", lettered_grade)
        print("Passing:", passing_grade)
        
main()
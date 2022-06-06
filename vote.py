
class Vote(object):
    candidate1 = input("Enter 1st candidate name:")
    candidate2 = input("Enter 2nd candidate name:")

    candidate1_votes = 0
    candidate2_votes = 0

    voters_id = [101, 102, 103, 104, 105, 106]
    number_of_voters = len(voters_id)

    voted = []

    while True:
        if not voters_id:
            print("Voting is over")

            if candidate1_votes > candidate2_votes:
                print(f"{candidate1} won the election with {candidate1_votes}")

            elif candidate1_votes < candidate2_votes:
                print(f"{candidate2} won the election with {candidate2_votes}")

            else:
                print("Tied!!!")
        else:
            voter = int(input("Enter your voter ID: "))

            if voter in voted:
                print("You already voted!!")
            else:
                if voter in voters_id:
                    print(f"1.{candidate1}\n2.{candidate2}")
                    choice = int(input("Enter your choice: "))

                    if choice == 1:
                        candidate1_votes += 1
                        print(f"You voted {candidate1}")
                    else:
                        candidate2_votes += 1
                        print(f"You voted {candidate2}")

                    voters_id.remove(voter)
                    voted.append(voter)
                else:
                    print("You are not allowed to vote")
import math

Human_Hearing_Threshold = 140 


def main_in_room():
    """ Stimulates the program if the user is in the classroom"""
    # input parameters
    lawnmower_power = float(input("enter lawnmower power in watts: "))
    material = input("enter room material(wood, glass, or bricks): ")
    distance = float(input("enter your distance from from the lawnmower in maters: "))

    # stimulate sound penetration
    sound_level = math.ceil(stimulate_sound_penetration_in_room(lawnmower_power, material, distance))

    # check if sound level exceeds hearing threshold or distance threshold
    if sound_level > Human_Hearing_Threshold:
        print(f"The sound level reaching you in the {material} room is {sound_level}. You are not hearing anything.")
    else:
        print(f"The sound level reaching you in the {material} room is {sound_level}. you are hearing the noise. ")


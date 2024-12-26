# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"
default saitZuddy = False
default saitCarme = False
default saitEmile = False
default saitFemme = False
default saitlettre = False
default emileConfession = False
default Carmedispute = False
$ emileConfession = false
$ knowsAboutChild = false
default knowsAboutChild = False
transform breathe_left:
    xpos 0.0                # Position à gauche
    linear 1.0 zoom 1.01     # Effet de respiration
    linear 1.0 zoom 1.0
    repeat

transform breathe_center:
    xpos 0.3                # Position au centre
    linear 1.0 zoom 1.01     # Effet de respiration
    linear 1.0 zoom 1.0
    repeat
transform breathe_right:
    xpos 0.6            # Position à droite
    linear 1.0 zoom 1.01     # Effet de respiration
    linear 1.0 zoom 1.0
    repeat




image bureau = "images/bg/bureau_détective.png"
image cirque_exterieur = "images/bg/cirqueextern.jpg"
image scene_zuddy = "images/bg/scene_zuddyetfin.jpg"
image manege = "images/bg/manège.jpg"
image scene_emile = "images/bg/scene_emile.jpg"
image bureauL = "images/bg/bureau_lucien.jpg"
image lucien = "images/bg/roulotte_lucien.jpg"
image scene_carme = "images/bg/scene_carme.jpg"
image scene_rosalie = "images/bg/scene_rosalie.jpg"
image chapiteau = "images/bg/endroit_abandonné.jpg"

# Déclarez les personnages utilisés dans le jeu.
define e = Character('Eileen', color="#398539")
define C = Character ('Christopher', color= "#01020f")
image Christopher = "images/personnage/Christopher/Christopher.png"
image Christopher_happy = "images/personnage/Christopher/Christopher_happy.png"
define B = Character ('Barbara', color= "#01020f")
image Barbara = "images/personnage/Barbara/barbara.png"
define O = Character ('Oliver', color= "#01020f")
image Oliver = "images/personnage/Oliver/Oliver.png"
image Oliver_angry = "images/personnage/Oliver/Oliver_angry.png"
image Oliver_talk = "images/personnage/Oliver/oliver_talk.png"
image Oliver_injuries = "images/personnage/Oliver/oliver_injuries.png"
define Carme = Character ('Carme', color="#01020f")
image Carme = "images/personnage/Carme/carme.png"
define Z = Character ('Zuddy', color= "#01020f")
image Zuddy = "images/personnage/Zuddy/Zuddy.png"
image Zuddy_chocked = "images/personnage/Zuddy/Zuddy_chocked.png"
image Zuddy_smile = "images/personnage/Zuddy/Zuddy_smile.png"
image Zuddy_eyes_closed = "images/personnage/Zuddy/Zuddy_eyes_closed.png"
image Zuddy_smile_eyes_closed = "images/personnage/Zuddy/Zuddy_smile_eyes_closed.png"
define E = Character ('Emile',color = "#01020f")
image Emile = "images/personnage/Emile/emile.png"
image Emile_happy = "images/personnage/Emile/emile_happy.png"
image Emile_shy = "images/personnage/Emile/emile_shy.png"
image Emile_blush= "images/personnage/Emile/emile_blush.png"
image Emile_smile_blush = "images/personnage/Emile/emile_smile_blush.png"
image Emile_regard_ailleurs = "images/personnage/Emile/emile_regard_ailleurs.png"
define R = Character ('Rosalie', color = "#01020f")
image Rosalie ="images/personnage/Rosalie/Rosalie.png"
image Rosalie_angry ="images/personnage/Rosalie/Rosalie_a.png"
image Rosalie_lie ="images/personnage/Rosalie/Rosalie_lie.png"
image Rosalie_regard_ailleurs ="images/personnage/Rosalie/Rosalie_regard_ailleurs.png"
image Rosalie_serious ="images/personnage/Rosalie/Rosalie_serious.png"
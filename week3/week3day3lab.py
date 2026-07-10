import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# df = pd.read_csv("PG.csv")

# positive = (df["Return"] > 0).sum()
# negative = (df["Return"] < 0).sum()

# print("Positive:", positive)
# print("Negative:", negative)
# print("Standard Devation:", df["Return"].std())
# print("Mean:", df["Return"].mean())

# lessThan = (df["Return"] < -2 * df["Return"].std()).sum()
# moreThan = (df["Return"] > 2 * df["Return"].std()).sum()

# print("Outliers:", lessThan + moreThan)

def rank_words(string):
    words = string.split()
    my_dict = {

    }
    for word in words:
        scrubbed_word = ""
        chars = list(word)
        for char in chars:
            if (char.isalpha()):
                scrubbed_word += char.lower()
        if (my_dict.get(scrubbed_word) is None):
            my_dict[scrubbed_word] = 1
        elif (my_dict.get(scrubbed_word) > 0):
            my_dict[scrubbed_word] += 1
    print(my_dict)

    df = pd.DataFrame(list(my_dict.items()))
    fig, ax = plt.subplots(figsize=(10,5))
    ax.hist(df.iloc[:, 1])

    plt.show()

rank_words("""
The old ram stands looking down over rockslides, stupidly
triumphant. I blink. I stare in horror. "Scat!" I hiss. "Go
back to your cave, go back to your cowshed-whatever."
He cocks his head like an elderly, slow-witted king, considers the angles, decides to ignore me. I stamp. I hammer
the ground with my fists. I hurl a skull-size stone at him.
He will not budge. I shake my two hairy fists at the sky
and I let out a howl so unspeakable that the water at my
feet turns sudden ice and even I myself am left uneasy.
But the ram stays; the season is upon us. And so begins the
twelfth year of my idiotic war.
The pain of it! The stupidity!
           "Ah, well," I sigh, and shrug, trudge back to the trees.
Do not think my brains are squeezed shut, like the ram's,
by the roots of horns. Flanks atremble, eyes like stones, he
stares at as much of the world as he can see and feels it
surging in him, filling his chest as the melting snow fills
dried-out creekbeds, tickling his gross, lopsided balls and
charging his brains with the same unrest that made him
suffer last year at this time, and the year before, and the
year before that. (He's forgotten them all.) His hindparts
shiver with the usual joyful, mindless ache to mount whatever happens near-the storm piling up black towers to
the west, some rotting, docile stump, some spraddle-legged
ewe. I cannot bear to look. "Why can't these creatures discover a little dignity?" I ask the sky. The sky says nothing,
predictably. I make a face, uplift a defiant middle finger,
and give an obscene little kick. The sky ignores me, forever unimpressed. Him too I hate, the same as I hate these
brainless budding trees, these brattling birds.
Not, of course, that I fool myself with thoughts that I'm
more noble. Pointless, ridiculous monster crouched in the.
shadows, stinking of dead men, murdered children, martyred cows. (I am neither proud nor ashamed, understand.
One more dull victim, leering at seasons that never were
meant to be observed.) "Ah, sad one, poor old freak!" I
cry, and hug myself, and laugh, letting out salt tears, he
he! till I fall down gasping and sobbing. (It's mostly fake.)
           The sun spins mindlessly overhead, the shadows lengthen
and shorten as if by plan. Small birds, with a high-pitched
yelp, lay eggs. The tender grasses peek up, innocent yellow,
through the ground: the children of the dead. (It was just
here, this shocking green, that once when the moon was
tombed in clouds, I tore off sly old Athelgard's head. Here,
where the startling tiny jaws of crocuses snap at the latewinter sun like the heads of baby watersnakes, here I killed
the old woman with the irongray hair. She tasted of urine
and spleen, which made me spit. Sweet mulch for yellow
blooms. Such are the tiresome memories of a shadowshooter, earth-rim-roamer, walker of the world's weird
wall.) "Waaah!" I cry, with another quick, nasty face at
the sky, mournfully observing the way it is, bitterly remembering the way it was, and idiotically casting tomorrow's
nets. "Aargh! Yaww!" I reel, smash trees. Disfigured son
of lunatics. The big-boled oaks gaze down at me yellow
with morning, beneath complexity. "No offense," I say,
with a terrible, sycophantish smile, and tip an imaginary
hat.
It was not always like this, of course. On occasion it's
been worse.
No matter, no matter.
The doe in the clearing goes stiff at sight of my horridness, then remembers her legs and is gone. It makes me
cross. "Blind prejudice!" I bawl at the splintered sunlight
""")
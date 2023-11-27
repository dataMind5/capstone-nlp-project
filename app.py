import streamlit as st
import numpy as np
import joblib
from gensim.models import KeyedVectors

# make sure to move models from notebooks folder to App/models folder

# open spacy word processing model

nlp_stuff = open('models/nlp_file_25_nov_2023.pkl', 'rb')
nlp = joblib.load(nlp_stuff)

# open word2vec model

wv = KeyedVectors.load('models/wv_model.model')

# open classifier model

essay_classifier = open('models/essay_classifier_25_nov_2023.pkl', 'rb')
clf = joblib.load(essay_classifier)

def preprocess_and_vectorize(text):
    doc = nlp(text)

    filtered_tokens = []
    for token in doc:
        if token.is_stop or token.is_punct:
            continue
        filtered_tokens.append(token.lemma_)

    vectors = []
    for token in filtered_tokens:
        try:
            vectors.append(wv[token])
        except KeyError:
            continue

    # get mean vector of all words in essay

    return wv.get_mean_vector(vectors)

def predict_essay(new_text):
    new_text_vec = preprocess_and_vectorize(new_text)
    new_text_vec_2d = np.stack(new_text_vec)
    results = clf.predict(new_text_vec_2d.reshape(1, -1))
    return results[0]

st.title('Essay Grading App')

st.write("ROUGH ROAD AHEAD: Do Not Exceed Posted Speed Limit - by Joe Kurmaskie")

p1 = "FORGET THAT OLD SAYING ABOUT NEVER taking candy from strangers. No, a better piece of advice for the solo cyclist would be, “Never accept travel advice from a collection of old-timers who haven’t left the confines of their porches since Carter was in office.” It’s not that a group of old guys doesn’t know the terrain. With age comes wisdom and all that, but the world is a fluid place. Things change."
p2 = "At a reservoir campground outside of Lodi, California, I enjoyed the serenity of an early-summer evening and some lively conversation with these old codgers. What I shouldn’t have done was let them have a peek at my map. Like a foolish youth, the next morning I followed their advice and launched out at first light along a “shortcut” that was to slice away hours from my ride to Yosemite National Park."
p3 = "They’d sounded so sure of themselves when pointing out landmarks and spouting off towns I would come to along this breezy jaunt. Things began well enough. I rode into the morning with strong legs and a smile on my face. About forty miles into the pedal, I arrived at the first “town.” This place might have been a thriving little spot at one time—say, before the last world war—but on that morning it fit the traditional definition of a ghost town. I chuckled, checked my water supply, and moved on. The sun was beginning to beat down, but I barely noticed it. The cool pines and rushing rivers of Yosemite had my name written all over them."
p4 = "Twenty miles up the road, I came to a fork of sorts. One ramshackle shed, several rusty pumps, and a corral that couldn’t hold in the lamest mule greeted me. This sight was troubling. I had been hitting my water bottles pretty regularly, and I was traveling through the high deserts of California in June."
p5 = "I got down on my hands and knees, working the handle of the rusted water pump with all my strength. A tarlike substance oozed out, followed by brackish water feeling somewhere in the neighborhood of two hundred degrees. I pumped that handle for several minutes, but the water wouldn’t cool down. It didn’t matter. When I tried a drop or two, it had the flavor of battery acid."
p6 = "The old guys had sworn the next town was only eighteen miles down the road. I could make that! I would conserve my water and go inward for an hour or so—a test of my inner spirit."
p7 = "Not two miles into this next section of the ride, I noticed the terrain changing. Flat road was replaced by short, rolling hills. After I had crested the first few of these, a large highway sign jumped out at me. It read: ROUGH ROAD AHEAD: DO NOT EXCEED POSTED SPEED LIMIT."
p8 = "The speed limit was 55 mph. I was doing a water-depleting 12 mph. Sometimes life can feel so cruel. I toiled on. At some point, tumbleweeds crossed my path and a ridiculously large snake—it really did look like a diamondback—blocked the majority of the pavement in front of me. I eased past, trying to keep my balance in my dehydrated state."
p9 = "The water bottles contained only a few tantalizing sips. Wide rings of dried sweat circled my shirt, and the growing realization that I could drop from heatstroke on a gorgeous day in June simply because I listened to some gentlemen who hadn’t been off their porch in decades, caused me to laugh."
p10 = "It was a sad, hopeless laugh, mind you, but at least I still had the energy to feel sorry for myself. There was no one in sight, not a building, car, or structure of any kind. I began breaking the ride down into distances I could see on the horizon, telling myself that if I could make it that far, I’d be fine."
p11 = "Over one long, crippling hill, a building came into view. I wiped the sweat from my eyes to make sure it wasn’t a mirage, and tried not to get too excited. With what I believed was my last burst of energy, I maneuvered down the hill. In an ironic twist that should please all sadists reading this, the building—abandoned years earlier, by the looks of it—had been a Welch’s Grape Juice factory and bottling plant. A sandblasted picture of a young boy pouring a refreshing glass of juice into his mouth could still be seen."
p12 = "I hung my head."
p13 = "That smoky blues tune “Summertime” rattled around in the dry honeycombs of my deteriorating brain. I got back on the bike, but not before I gathered up a few pebbles and stuck them in my mouth. I’d read once that sucking on stones helps take your mind off thirst by allowing what spit you have left to circulate. With any luck I’d hit a bump and lodge one in my throat. It didn’t really matter. I was going to die and the birds would pick me clean, leaving only some expensive outdoor gear and a diary with the last entry in praise of old men, their wisdom, and their keen sense of direction. I made a mental note to change that paragraph if it looked like I was going to lose consciousness for the last time. Somehow, I climbed away from the abandoned factory of juices and dreams, slowly gaining elevation while losing hope. Then, as easily as rounding a bend, my troubles, thirst, and fear were all behind me."
p14 = "GARY AND WILBER’S FISH CAMP—IF YOU WANT BAIT FOR THE BIG ONES, WE’RE YOUR BEST BET! “And the only bet,” I remember thinking. As I stumbled into a rather modern bathroom and drank deeply from the sink, I had an overwhelming urge to seek out Gary and Wilber, kiss them, and buy some bait—any bait, even though I didn’t own a rod or reel. An old guy sitting in a chair under some shade nodded in my direction. Cool water dripped from my head as I slumped against the wall beside him. “Where you headed in such a hurry?” “Yosemite,” I whispered. “Know the best way to get there?” I watched him from the corner of my eye for a long moment. He was even older than the group I’d listened to in Lodi. “Yes, sir! I own a very good map.” And I promised myself right then that I’d always stick to it in the future."
p15 = "“Rough Road Ahead” by Joe Kurmaskie, from Metal Cowboy, copyright © 1999 Joe Kurmaskie."


st.write(p1)
st.write(p2)
st.write(p3)
st.write(p4)
st.write(p5)
st.write(p6)
st.write(p7)
st.write(p8)
st.write(p9)
st.write(p10)
st.write(p11)
st.write(p12)
st.write(p13)
st.write(p14)
st.write(p15)

st.subheader('Prompt')

st.write('Write a response that explains how the features of the setting affect the cyclist. In your response, include examples from the essay that support your conclusion.')
st.write('Rubric Guidelines')
st.write('Score 3: The response demonstrates an understanding of the complexities of the text.')
st.write('- Addresses the demands of the question')
st.write('- Uses expressed and implied information from the text')
st.write('- Clarifies and extends understanding beyond the literal')
st.write('Score 2: The response demonstrates a partial or literal understanding of the text.')
st.write('- Addresses the demands of the question, although may not develop all parts equally')
st.write('- Uses some expressed or implied information from the text to demonstrate understanding')
st.write('- May not fully connect the support to a conclusion or assertion made about the text(s)')
st.write('Score 1: The response shows evidence of a minimal understanding of the text.')
st.write('- May show evidence that some meaning has been derived from the text')
st.write('- May indicate a misreading of the text or the question')
st.write('- May lack information or explanation to support an understanding of the text in relation to the question')
st.write('Score 0: The response is completely irrelevant or incorrect, or there is no response.')

with st.form(key='essay_clf_form'):
    raw_text = st.text_area('Type Your Response Here')
    submit_text = st.form_submit_button(label='Grade')

if submit_text:

    prediction = predict_essay(raw_text)

    col1,col2 = st.columns(2)

    with col1:
        st.success('Essay Grade')
        st.subheader(prediction)

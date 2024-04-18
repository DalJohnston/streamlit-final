#Smash streamlit app

import pandas as pd
import plotly.express as px
import streamlit as st

st.title('Super Smash Bros. Ultimate Fighter Data')


#Data
smashurl = 'https://raw.githubusercontent.com/DalJohnston/streamlit-final/main/smash.csv'
smashurlsurl = 'https://raw.githubusercontent.com/DalJohnston/streamlit-final/main/smashurls.csv'

smash = pd.read_csv(smashurl)
smashurls = pd.read_csv(smashurlsurl)

#sidebar
st.sidebar.title('Extras')

st.sidebar.header('Learn More About a Fighter! \U0001F94A')
ultimate = st.sidebar.selectbox('Fighter', options=smashurls['Fighter'], index=0)
funurl = smashurls[smashurls['Fighter']==ultimate]['URL'].to_list()[0]

st.sidebar.link_button("Go!", funurl)


st.sidebar.header('Competitive Smash Ultimate \U0001F4A5')
st.sidebar.link_button("Captain Falcon v. Sephiroth", 'https://www.youtube.com/watch?v=LOKP6HQCa6Y')
st.sidebar.link_button("Roy v. Joker", 'https://www.youtube.com/watch?v=kxQO6l4UlNI')
st.sidebar.link_button("Palutena v. Richter", 'https://www.youtube.com/watch?v=ZWgDOfE1ZxE')

#Variable explanations

st.sidebar.header('Variable Info \U0001F4D8')
infovar = st.sidebar.selectbox('Select Variable', options=smash.columns, index=0)

if infovar == 'Fighter':
    st.sidebar.markdown('''Fighter name.''')
if infovar == 'Tier':
    st.sidebar.markdown('''A category referring to how effective a fighter is in competitive play. 1 is the best tier; 7 is the worst.''')
if infovar == 'Grab Range':
    st.sidebar.markdown('''All fighters have the ability to grab other fighters while grounded and throw them.  Grab range is the maximum relative lateral range that each fighter can make a grab from.''')
if infovar == 'Base Air Acceleration':
    st.sidebar.markdown('''How quickly a fighter accelerates in the air without the player doing anything.''')
if infovar == 'Additional Air Acceleration':
    st.sidebar.markdown('''How quickly a fighter accelerates in the air based on how much the player tilts the control stick.''')
if infovar == 'Max Air Acceleration':
    st.sidebar.markdown('''Combination of base and additional air acceleration values.''')
if infovar == 'Air Speed':
    st.sidebar.markdown('''How fast a fighter can move laterally while airborne.''')
if infovar == 'Fall Speed':
    st.sidebar.markdown('''How fast a fighter falls to the ground without the player doing anything.''')
if infovar == 'Fast Fall Speed':
    st.sidebar.markdown('''Fall speed when a player executes a "fast fall." Players can make their fighter fall to the ground faster by tilting the control stick downward.''')
if infovar == 'Gravity':
    st.sidebar.markdown('''How fast a falling fighter reaches their fast fall speed.''')
if infovar == 'Full Hop Height':
    st.sidebar.markdown('''Relative vertical height of a fighter's full basic jump.''')
if infovar == 'Short Hop Height':
    st.sidebar.markdown('''Relative vertical height of a fighter's short jump. A short hop is done when the jump button is pressed quickly for the fighter to perform a smaller hop than the full standard jump.''')
if infovar == 'Double Jump Height':
    st.sidebar.markdown('''Relative vertical height of a fighter's midair jump.''')
if infovar == 'Full Hop Duration':
    st.sidebar.markdown('''How many frames it takes for a fighter to complete a full hop.''')
if infovar == 'Short Hop Duration':
    st.sidebar.markdown('''How many frames it takes for a fighter to complete a short hop.''')
if infovar == 'Fast Fall Duration from Full Hop':
    st.sidebar.markdown('''How many frames it takes for a fighter to complete a full hop with a fast fall.''')
if infovar == 'Weight':
    st.sidebar.markdown('''Relative in-game measure of how "heavy" a fighter is. Fighters with more weight are harder to knock back.''')
if infovar == 'Walk Speed':
    st.sidebar.markdown('''Relative measure of how fast a fighter can walk.''')
if infovar == 'Initial Dash Speed':
    st.sidebar.markdown('''Relative measure of how fast a fighter can dash, or run, the instant the player tilts the control stick.''')
if infovar == 'Dash Frames':
    st.sidebar.markdown('''How many frames it takes a fighter to complete their grounded dash animation.''')
if infovar == 'Pivot Dash Frames':
    st.sidebar.markdown('''How many frames it takes a fighter to turn around and dash in the opposite direction''')
if infovar == 'DLC':
    st.sidebar.markdown('''Whether or not a fighter is paid "downloadable content" that comes separate from the basic game.''')



#scatterplot

st.markdown('''\U0001F525 Below is some fighter data for the popular 2018 fighting game: "Super Smash Bros. Ultimate." \U0001F525''')

st.markdown('''While marketed towards casual players, Super Smash Bros. Ultimate has an absurdly intense competitive scene with some even making it their life’s mission to become the very best.  As such, there exists within the game’s community a perpetual debate about who the best players are, what the best strategies are, and **especially** what fighting characters you need to use to be able to win.  The graphics below are meant to help us understand this last question in particular.''')

st.header('''Interactive Scatterplot''')
st.markdown('''Basic comparison of fighter data categories. Hover over a point to see specific values.''')

fig = px.scatter(smash, x='Weight', y='Tier', color_discrete_sequence=['#FF0000'],
                 title='', labels={'x': 'X Axis', 'y': 'Y Axis'})


optiondf = smash.drop(columns=['Fighter', 'DLC'])

xvar, yvar = st.columns(2)
with xvar:
    x_axis = st.selectbox('X Axis', options=optiondf.columns, index=optiondf.columns.get_loc('Weight'))
with yvar:
    y_axis = st.selectbox('Y Axis', options=optiondf.columns, index=optiondf.columns.get_loc('Tier'))

fig.update_traces(x=smash[x_axis], y=smash[y_axis])
fig.update_layout(xaxis_title=x_axis, yaxis_title=y_axis)





#Make Fighter name display when hovering over points
fig.update_traces(customdata=smash[['Fighter']]) #custom data associated with data point
fig.update_traces(hovertemplate="<br>".join([ #formats hover output
    "Fighter: %{customdata[0]}",
    f"{x_axis}: %{{x}}",
    f"{y_axis}: %{{y}}"
]))

st.plotly_chart(fig)
####################################################


#Individual Character Data
st.header('Individual Fighter Data')
st.markdown('Explore some specific stats for one or more fighters.')

characters = st.multiselect('Choose Your Fighters!', options=smash['Fighter'], default=['Mario', 'Link'])
character_data = smash[smash['Fighter'].isin(characters)]
st.dataframe(character_data)

####################################################

#Tier graphs
st.header('''Tier Rankings and Desirable Fighter Attributes''')
st.markdown('''What qualities really matters in a top-tier champion? To find that out, I decided to compare fighter tiers to other values. Tier refers to a fighter's ranking category. The best fighters are in tier 1, and the worst are in tier 7.''')

factor = st.radio("Explore some notable and interesting influencers of tier.",
                  options=['Weight', 'Initial Dash Speed', 'Max Air Acceleration'],
                  captions=['Float like a butterfly?', '''How about that dash dance?''', 'Versatility when it counts.'])

if factor == 'Weight':
    weightbox = px.box(smash, x='Tier', y='Weight', color='Tier',
                  title='Tier vs Weight', labels={'x': 'Tier', 'y':'Weight'})
    weightbox.update_traces(showlegend=False)
    st.plotly_chart(weightbox)
    st.markdown('''From the exploratory boxplot, it does seem like fighters of a heavier weight class tend to be placed in a lower tier.  There appears to be more of an even distribution among the middle tiers, even continuing into the top tiers with perhaps a couple of lighter fighters being more favorable.  Sorry, Mike Tyson.  It looks like being a heavyweight might not be as favorable in this kind of fight.

This makes sense, though.  Smash Ultimate is considered to be very movement-based, and heavier fighters can tend to be bigger and slower.  Many winning strategies are centered around confusing your opponent with quick and erratic movement patterns that heavier fighters just can’t pull off as well. 
''')

elif factor == 'Initial Dash Speed':
    dashbox = px.box(smash, x='Tier', y='Initial Dash Speed', color='Tier',
                 title='Tier vs Initial Dash Speed', labels={'x': 'Tier', 'y':'Initial Dash Speed'})
    dashbox.update_traces(showlegend=False)
    st.plotly_chart(dashbox)
    st.markdown('''A very common and effective movement strategy in Smash is called dash dancing.  Dash dancing involves a fighter’s initial dash speed.''')
    st.link_button("More About Dash Dancing", 'https://www.youtube.com/watch?v=mmwfe6gOTUA')
    st.markdown('''What I found surprised me at first, but it makes sense.  Here, it seems that fighters with the best dash dances tend to be placed in middle tiers.  Among all of the middle tiers (6 to 2) there does seem to be a slight upward trend in initial dash speed, but the top and bottom tier do not follow this trend at all.  In fact, it seems like the best fighters in the game almost have a worse dash dance than the worst fighters.  To me, this indicates that while quick movement is certainly important for a good fighter to have, it isn’t quite the deciding factor in what pushes a them over the edge to make them the very best.''')



elif factor == 'Max Air Acceleration':
    maxbox = px.box(smash, x='Tier', y='Max Air Acceleration', color='Tier',
                    title='Tier vs Max Air Acceleration', labels={'x': 'Tier', 'y':'Max Air Acceleration'})
    maxbox.update_traces(showlegend=False)
    st.plotly_chart(maxbox)
    st.markdown('''Semper gumby, versatility is a virtue, and it seems like that holds true for Smash Ultimate as well.  It's hard to put a concrete number or rating on versatility, but if we needed to choose, then max air acceleration would be a compelling candidate.  Just take a look at some versatile gameplay from Jigglypuff, the fighter with the highest max air acceleration in the game.''')
    st.link_button("Check out some versatile Jigglypuff! \U0001F33A", 'https://www.youtube.com/watch?v=Z_5YHlNN9PY')
    st.markdown('''Maximum air acceleration just refers to how fast a character can reach a top speed in midair, which can be paramount for a player in extending their attack combo or escaping from an opponent's, especially since the most fatal of these combos happen in the air.  If you aren't able to escape enough unfriendly combos or finish enough of your own, you'll soon find yourself at the bottom of the food chain.''')




#DLC graphs
st.header('The DLC Dilemma')

st.markdown('''Since the release of Super Smash Bros. Ultimate in 2018, quite a few additional fighters have been added to the game to make the roster as big as it is today.  However, these fighters were included as paid DLC, or downloadable content.''')
st.markdown('''In other words, to get the extra fighters, your wallet needs to step into the ring.  Most consider Smash Ultimate to be a competitively balanced game, even with the extra fighters, but still, there has been a lot of debate as to whether these DLC characters are “stronger” so that loyal customers feel like they are getting their money’s worth.''')
st.markdown('''Are the fighters you pay extra for really worth your money? You decide. \U0001F4B0''')

smashbox = smash
smashbox['DLC'] = smash['DLC'].map({1: 'Yes', 0: 'No'})

figbox = px.box(smashbox, x='DLC', y='Tier',
                title='A Difference with DLC?', labels={'x': 'DLC', 'y':'Y Axis'})

yvar = st.selectbox('Choose Character Stat', options=optiondf.columns, index=optiondf.columns.get_loc('Tier'))

figbox.update_traces(y=optiondf[yvar])
figbox.update_layout(yaxis_title=yvar)

st.plotly_chart(figbox)


##Filter the Dataset

#options for columns to include (dropping/adding columns) with multiselect
st.header('Filter Data')
fighterless = smash.drop(columns=['Fighter'])

cols = st.multiselect('Select Columns', options=fighterless.columns, default=['DLC', 'Tier', 'Initial Dash Speed', 'Max Air Acceleration'])
filterset2 = smash[['Fighter']+cols]


#filtering using groupby Fighter and then sorting values
filter = st.selectbox('Filter by...', options=filterset2.columns, index=1)
    
displaydata = filterset2.groupby('Fighter').first().sort_values(by=filter)

st.dataframe(displaydata)


#######################################################################
# st.header('Individual Character Data')
# characters = st.multiselect('Choose Your Fighters!', options=smash['Fighter'], default=['Mario', 'Link'])
# character_data = smash[smash['Fighter'].isin(characters)]
# st.dataframe(character_data)
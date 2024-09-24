import streamlit as st
import pandas as pd
import joblib

# تحميل النموذج المدرب باستخدام joblib
model = joblib.load('random_forest_model.pkl')

# باقي الكود كما هو
st.title('Mobile Price Classification')

st.write("""
    This app uses a trained machine learning model to classify mobile phones into different price ranges based on the phone's features.
""")

battery_power = st.number_input('Battery Power (mAh)', min_value=500, max_value=5000, step=100)
blue = st.selectbox('Bluetooth', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
clock_speed = st.slider('Clock Speed (GHz)', min_value=0.5, max_value=3.0, step=0.1)
dual_sim = st.selectbox('Dual SIM', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
fc = st.number_input('Front Camera (MP)', min_value=0, max_value=20, step=1)
four_g = st.selectbox('4G Support', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
int_memory = st.number_input('Internal Memory (GB)', min_value=2, max_value=256, step=2)
m_dep = st.slider('Mobile Depth (cm)', min_value=0.1, max_value=1.0, step=0.1)
mobile_wt = st.number_input('Mobile Weight (g)', min_value=80, max_value=300, step=5)
n_cores = st.number_input('Number of Cores', min_value=1, max_value=8, step=1)
pc = st.number_input('Primary Camera (MP)', min_value=0, max_value=50, step=1)
px_height = st.number_input('Pixel Height', min_value=0, max_value=1960, step=10)
px_width = st.number_input('Pixel Width', min_value=0, max_value=1960, step=10)
ram = st.number_input('RAM (MB)', min_value=256, max_value=8000, step=256)
sc_h = st.number_input('Screen Height (cm)', min_value=5, max_value=20, step=1)
sc_w = st.number_input('Screen Width (cm)', min_value=5, max_value=20, step=1)
talk_time = st.number_input('Talk Time (hours)', min_value=2, max_value=50, step=1)
three_g = st.selectbox('3G Support', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
touch_screen = st.selectbox('Touch Screen', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')
wifi = st.selectbox('WiFi Support', [0, 1], format_func=lambda x: 'Yes' if x == 1 else 'No')

# جمع المدخلات في DataFrame
input_data = pd.DataFrame({
    'battery_power': [battery_power],
    'blue': [blue],
    'clock_speed': [clock_speed],
    'dual_sim': [dual_sim],
    'fc': [fc],
    'four_g': [four_g],
    'int_memory': [int_memory],
    'm_dep': [m_dep],
    'mobile_wt': [mobile_wt],
    'n_cores': [n_cores],
    'pc': [pc],
    'px_height': [px_height],
    'px_width': [px_width],
    'ram': [ram],
    'sc_h': [sc_h],
    'sc_w': [sc_w],
    'talk_time': [talk_time],
    'three_g': [three_g],
    'touch_screen': [touch_screen],
    'wifi': [wifi]
})

# عرض التوقع عند الضغط على زر
if st.button('Predict Price Range'):
    prediction = model.predict(input_data)
    st.write(f'The predicted price range is: {prediction[0]}')

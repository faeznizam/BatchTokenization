# 1. import module
from dearpygui import dearpygui as dpg

# 2. create context - this will initiate dpg environment
dpg.create_context()

# 3. create button
def on_button_click(sender, app_data, user_data):
    print('Clicked')

# 4. create main window
with dpg.window(label='test', width=200, height=200):
    dpg.add_button(label='Click Me', callback=on_button_click)

# 5. create and start application
dpg.create_viewport(title='Dear PyGui Demo', width=300, height=150)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
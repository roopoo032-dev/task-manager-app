import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Главное Меню', font_size='24sp'))
        
        buttons = [
            ('Создать задачу', 'create'),
            ('Просмотреть задачи', 'view'), 
            ('Настройки', 'settings'),
            ('Выход', 'exit')
        ]
        
        for text, screen in buttons:
            btn = Button(text=text, size_hint_y=None, height=50)
            btn.bind(on_release=lambda x, s=screen: setattr(self.manager, 'current', s))
            layout.add_widget(btn)
        
        self.add_widget(layout)

class CreateTaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Создать задачу', font_size='24sp'))
        
        self.title_input = TextInput(hint_text='Название задачи', size_hint_y=None, height=40)
        layout.add_widget(self.title_input)
        
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        create_btn = Button(text='Создать')
        create_btn.bind(on_release=self.create_task)
        btn_layout.add_widget(create_btn)
        
        back_btn = Button(text='Назад')
        back_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        btn_layout.add_widget(back_btn)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)
    
    def create_task(self, instance):
        print(f"Создана задача: {self.title_input.text}")

  class ViewTasksScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Мои задачи', font_size='24sp'))
        
        scroll = ScrollView()
        content = BoxLayout(orientation='vertical', size_hint_y=None)
        content.bind(minimum_height=content.setter('height'))
        
        tasks = ['Пример задачи 1', 'Пример задачи 2']
        for task in tasks:
            lbl = Label(text=task, size_hint_y=None, height=40)
            content.add_widget(lbl)
        
        scroll.add_widget(content)
        layout.add_widget(scroll)
        
        back_btn = Button(text='Назад', size_hint_y=None, height=50)
        back_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Настройки', font_size='24sp'))
        layout.add_widget(Label(text='Менеджер задач v1.0'))
        
        back_btn = Button(text='Назад', size_hint_y=None, height=50)
        back_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)

class ExitScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        layout.add_widget(Label(text='Выйти из приложения?', font_size='24sp'))
        
        btn_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        yes_btn = Button(text='Да')
        yes_btn.bind(on_release=lambda x: exit())
        btn_layout.add_widget(yes_btn)
        
        no_btn = Button(text='Нет')
        no_btn.bind(on_release=lambda x: setattr(self.manager, 'current', 'menu'))
        btn_layout.add_widget(no_btn)
        
        layout.add_widget(btn_layout)
        self.add_widget(layout)

class TaskManagerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(CreateTaskScreen(name='create'))
        sm.add_widget(ViewTasksScreen(name='view'))
        sm.add_widget(SettingsScreen(name='settings'))
        sm.add_widget(ExitScreen(name='exit'))
        return sm

if __name__ == '__main__':
    TaskManagerApp().run()
    

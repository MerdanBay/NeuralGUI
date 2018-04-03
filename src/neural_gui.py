import wx


class Neural_Trainer(wx.Frame):

    def __init__(self, parent, title):
        super(Neural_Trainer, self).__init__(parent, title=title,
                                             size=(480, 400))

        self.InitUI()
        self.Centre()
        self.Show()

    def Siezer_panel(self, sizer, panel):
        self.title_label = wx.StaticText(panel, label="Neural Trainer")
        sizer.Add(self.title_label, pos=(0, 0), flag=wx.TOP | wx.LEFT | wx.BOTTOM,
                  border=15)

        self.line = wx.StaticLine(panel)
        sizer.Add(self.line, pos=(1, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.BOTTOM, border=10)

        return sizer, panel

    def Import_model(self, sizer, panel):
        model_label = wx.StaticText(panel, label="Model")
        sizer.Add(model_label, pos=(2, 0), flag=wx.LEFT, border=10)

        self.model_import_button = wx.Button(panel, label="Browse")

        self.Bind(event=wx.EVT_BUTTON, handler=self.File_open, id=self.model_import_button.GetId())
        sizer.Add(self.model_import_button, pos=(2, 4),
                  flag=wx.TOP | wx.RIGHT, border=5)

        self.model_path = wx.TextCtrl(panel)
        sizer.Add(self.model_path, pos=(2, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND)

        return sizer, panel

    def Import_weight(self, sizer, panel):
        self.weight_label = wx.StaticText(panel, label="Weight")
        sizer.Add(self.weight_label, pos=(3, 0), flag=wx.LEFT | wx.TOP, border=10)

        self.weight_import_button = wx.Button(panel, label="Browse")
        self.Bind(event=wx.EVT_BUTTON, handler=self.File_open, id=self.weight_import_button.GetId())
        sizer.Add(self.weight_import_button, pos=(3, 4),
                  flag=wx.TOP | wx.RIGHT, border=5)

        self.weight_path = wx.TextCtrl(panel)
        sizer.Add(self.weight_path, pos=(3, 1), span=(1, 3), flag=wx.TOP | wx.EXPAND,
                  border=5)
        return sizer, panel

    def Import_database(self, sizer, panel):
        self.database_label = wx.StaticText(panel, label="DataBase")
        sizer.Add(self.database_label, pos=(4, 0), flag=wx.TOP | wx.LEFT, border=10)

        self.database_button = wx.Button(panel, label="Browse")
        self.Bind(event=wx.EVT_BUTTON, handler=self.File_open, id=self.database_button.GetId())
        sizer.Add(self.database_button, pos=(4, 4),
                  flag=wx.TOP | wx.RIGHT, border=5)

        self.database_path = wx.TextCtrl(panel)
        sizer.Add(self.database_path, pos=(4, 1), span=(1, 3),
                  flag=wx.TOP | wx.EXPAND, border=5)
        return sizer, panel

    def Tensorboard_save(self, sizer, panel):
        self.tensorboard_label = wx.StaticText(panel, label="Tensorboard")
        sizer.Add(self.tensorboard_label, pos=(5, 0), flag=wx.TOP | wx.LEFT, border=10)

        self.tensorboar_button = wx.Button(panel, label="Browse")
        self.Bind(event=wx.EVT_BUTTON, handler=self.File_open, id=self.tensorboar_button.GetId())
        sizer.Add(self.tensorboar_button, pos=(5, 4),
                  flag=wx.TOP | wx.RIGHT, border=5)

        self.tensorboard_path = wx.TextCtrl(panel)
        sizer.Add(self.tensorboard_path, pos=(5, 1), span=(1, 3),
                  flag=wx.TOP | wx.EXPAND, border=5)
        return sizer, panel
    
    def Hyper_paramers(self, sizer, panel):
        self.sb = wx.StaticBox(panel, label=" Attributes")

        self.boxsizer = wx.StaticBoxSizer(self.sb, wx.VERTICAL)
        self.boxsizer.Add(wx.CheckBox(panel, label="Train"),
                     flag=wx.LEFT | wx.TOP, border=5)
        self.boxsizer.Add(wx.CheckBox(panel, label="Predict"),
                     flag=wx.LEFT, border=5)
        self.boxsizer.Add(wx.CheckBox(panel, label="Float32"),
                     flag=wx.LEFT, border=5)

        sizer.Add(self.boxsizer, pos=(6, 0), span=(1, 5),
                  flag=wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, border=10)

        self.load_model = wx.Button(panel, label='Pre-load')
        self.Bind(event=wx.EVT_BUTTON, handler=self.Creat_neural, id=self.load_model.GetId())
        sizer.Add(self.load_model, pos=(8, 0), flag=wx.LEFT, border=10)

        self.start_button = wx.Button(panel, label="Start")
        sizer.Add(self.start_button, pos=(8, 3))

        self.cancel_button = wx.Button(panel, label="Cancel")
        sizer.Add(self.cancel_button, pos=(8, 4), span=(1, 1),
                  flag=wx.BOTTOM | wx.RIGHT, border=5)
        return sizer, panel

    def Creat_neural(self):
        flag = 0
        if self.model_path.GetValue():
            flag = 1
        else:
            wx.MessageBox('please chose model file')
            flag = 0

        if self.weight_path.GetValue():
            flag = 1
        else:
            wx.MessageBox('please chose weight file')
            flag = 0

        if self.database_path.GetValue():
            flag = 1
        else:
            wx.MessageBox('please chose database')
            flag = 0

        if flag == 1:
            self.Nerural_Kernel(self)

    def File_open(self, event):
        current_event_id = event.GetId()
        if current_event_id == self.model_import_button.GetId():
            with wx.FileDialog(self, "Choose a file to open", "./",
                           "", "*.*", wx.FD_OPEN) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    self.model_path.write('/'.join((directory, filename)))

        if current_event_id == self.weight_import_button.GetId():
            with wx.FileDialog(self, "Choose a file to open", "./",
                           "", "*.*", wx.FD_OPEN) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    self.weight_path.write('/'.join((directory, filename)))

        if current_event_id == self.database_button.GetId():
            with wx.FileDialog(self, "Choose a file to open", "./",
                           "", "*.*", wx.FD_OPEN) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    self.database_path.write('/'.join((directory, filename)))

        if current_event_id == self.tensorboar_button.GetId():
            with wx.DirDialog (None, "Choose input directory", "",
                               wx.DD_DEFAULT_STYLE | wx.DD_DIR_MUST_EXIST) as dlg:
                if dlg.ShowModal() == wx.ID_OK:
                    self.tensorboard_path.write(dlg.GetPath())

    def InitUI(self):
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(5, 5)

        sizer, panel = self.Siezer_panel(sizer, panel)
        sizer, panel = self.Import_model(sizer, panel)
        sizer, panel = self.Import_weight(sizer, panel)
        sizer, panel = self.Import_database(sizer, panel)
        sizer, panel = self.Hyper_paramers(sizer, panel)
        sizer, panel = self.Tensorboard_save(sizer, panel)

        sizer.AddGrowableCol(2)
        panel.SetSizer(sizer)
        


    class Nerural_Kernel():
        def __init__(self, GUI):
                import pandas as pd
                # import data_generator as dg
                from keras.models import load_model
                from keras.backend import set_floatx
                from tensorflow import ConfigProto


        # self.neural_model = load_model(model_path)
        # self.neural_model.load_weights(weight_path)
        # dataSet = ds.Handler(5000, ['20180124'])
        # tensorboard =  



if __name__ == '__main__':

    app = wx.App()
    NT = Neural_Trainer(None, title="Neural Network")
    app.MainLoop()

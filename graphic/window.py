from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QGraphicsEllipseItem, QGraphicsTextItem, QDialog, \
    QVBoxLayout, QPushButton, QWidget, QLineEdit, QGraphicsRectItem, QLabel


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.scene = QGraphicsScene(self)
        self.view = MyGraphicsView(self.scene)

        button = QPushButton('Добавить ограничение')
        button.clicked.connect(self.on_open_dialog_button_clicked)

        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(self.view)

        self.setGeometry(100, 100, 600, 800)
        self.setWindowTitle('Лаба в PyQt5')

        self.setLayout(layout)
        self.show()

    def mousePressEvent(self, event):
        global_point = event.globalPos()
        view_point = self.view.mapFromGlobal(global_point)
        scene_point = self.view.mapToScene(view_point)

        ellipse = QGraphicsEllipseItem(scene_point.x() - 5, scene_point.y() - 5, 10, 10)
        ellipse.setBrush(Qt.red)
        self.scene.addItem(ellipse)

        text = QGraphicsTextItem(f'({scene_point.x()}, {scene_point.y()})')
        text.setPos(scene_point.x() + 10, scene_point.y() + 10)
        self.scene.addItem(text)

    def on_open_dialog_button_clicked(self):
        dialog = MyDialog()
        result = dialog.exec_()

        if result == QDialog.Accepted:
            rectangle_data = dialog.getRectangleData()
            print(f"Получены данные: {rectangle_data}")

            rect_data = [int(x) for x in rectangle_data.split()]
            rect = QGraphicsRectItem(rect_data[0], rect_data[1], rect_data[2], rect_data[3])
            self.scene.addItem(rect)


class MyGraphicsView(QGraphicsView):
    def __init__(self, scene):
        super().__init__(scene)
        self.setRenderHint(QPainter.Antialiasing, True)
        self.setRenderHint(QPainter.SmoothPixmapTransform, True)
        self.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Диалоговое окно')

        layout = QVBoxLayout()

        self.label1 = QLabel('Введите координату x:', self)
        self.input1 = QLineEdit(self)
        self.label2 = QLabel('Введите координату y:', self)
        self.input2 = QLineEdit(self)
        self.label3 = QLabel('Введите ширину пряmоугольника', self)
        self.input3 = QLineEdit(self)
        self.label4 = QLabel('Введите высоту пряmоугольника', self)
        self.input4 = QLineEdit(self)

        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.label3)
        layout.addWidget(self.input3)
        layout.addWidget(self.label4)
        layout.addWidget(self.input4)

        button = QPushButton('Принять')
        button.clicked.connect(self.accept)

        layout.addWidget(button)

        self.setLayout(layout)

    def getRectangleData(self):
        return f"{self.input1.text()} {self.input2.text()} {self.input3.text()} {self.input4.text()}"

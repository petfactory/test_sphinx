import sys

import PySide2.QtWidgets as QtWidgets

class CollapseFrame(QtWidgets.QFrame):
	'''docstring for CollapseFrame'''

	def __init__(self, name, height, *args, **kwargs):
		super(CollapseFrame, self).__init__(*args, **kwargs)
		self._name = name
		self._height = height

	def get_info(self):
		'''docstring for get_info'''
		return '{} {}'.format(self._name, self._height)

		

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    w = CollapseFrame('Pet', 20)
    print(w.get_info())
    w.show()
    app.exec_()
import sys
from importlib import import_module
from types import ModuleType

_QT_MODULE = None

# Widgets supported by Qt4 and Qt5
_WIDGETS = ['QAbstractButton', 'QGraphicsAnchor', 'QStyleOptionGroupBox',
            'QAbstractGraphicsShapeItem', 'QGraphicsAnchorLayout', 'QMainWindow',
            'QStyleOptionHeader', 'QAbstractItemDelegate', 'QGraphicsBlurEffect',
            'QMdiArea', 'QStyleOptionMenuItem', 'QAbstractItemView', 'QGraphicsColorizeEffect',
            'QMdiSubWindow', 'QStyleOptionProgressBar', 'QAbstractScrollArea',
            'QGraphicsDropShadowEffect', 'QMenu', 'QStyleOptionRubberBand', 'QAbstractSlider',
            'QGraphicsEffect', 'QMenuBar', 'QStyleOptionSizeGrip', 'QAbstractSpinBox',
            'QGraphicsEllipseItem', 'QMessageBox', 'QStyleOptionSlider', 'QAction',
            'QGraphicsGridLayout', 'QMouseEventTransition', 'QStyleOptionSpinBox',
            'QActionGroup', 'QGraphicsItem', 'QStyleOptionTab', 'QApplication',
            'QStyleOptionTabBarBase', 'QGraphicsItemGroup', 'QStyleOptionTabWidgetFrame',
            'QGraphicsLayout', 'QStyleOptionTitleBar', 'QGraphicsLayoutItem', 'QPanGesture',
            'QStyleOptionToolBar', 'QBoxLayout', 'QGraphicsLineItem', 'QPinchGesture',
            'QStyleOptionToolBox', 'QGraphicsLinearLayout', 'QPlainTextDocumentLayout',
            'QStyleOptionToolButton', 'QButtonGroup', 'QGraphicsObject', 'QPlainTextEdit',
            'QStyleOptionViewItem', 'QGraphicsOpacityEffect', 'QProgressBar', 'QStylePainter',
            'QCalendarWidget', 'QGraphicsPathItem', 'QProgressDialog', 'QStyledItemDelegate',
            'QGraphicsPixmapItem', 'QGraphicsPolygonItem', 'QPushButton', 'QCheckBox',
            'QGraphicsProxyWidget', 'QRadioButton', 'QSwipeGesture', 'QColorDialog',
            'QGraphicsRectItem', 'QSystemTrayIcon', 'QGraphicsRotation', 'QTabBar', 'QColumnView',
            'QGraphicsScale', 'QRubberBand', 'QComboBox', 'QGraphicsScene', 'QTabWidget',
            'QCommandLinkButton', 'QGraphicsSceneContextMenuEvent', 'QScrollArea', 'QTableView',
            'QCommonStyle', 'QGraphicsSceneDragDropEvent', 'QScrollBar', 'QTableWidget', 'QCompleter',
            'QGraphicsSceneEvent', 'QTableWidgetItem', 'QGraphicsSceneHelpEvent',
            'QTableWidgetSelectionRange', 'QGraphicsSceneHoverEvent', 'QDataWidgetMapper',
            'QGraphicsSceneMouseEvent', 'QShortcut', 'QTapAndHoldGesture', 'QDateEdit',
            'QGraphicsSceneMoveEvent', 'QSizeGrip', 'QTapGesture', 'QDateTimeEdit',
            'QGraphicsSceneResizeEvent', 'QSizePolicy', 'QTextBrowser', 'QDesktopWidget',
            'QGraphicsSceneWheelEvent', 'QSlider', 'QTextEdit', 'QDial', 'QGraphicsSimpleTextItem',
            'QSpacerItem', 'QTimeEdit', 'QDialog', 'QGraphicsTextItem', 'QSpinBox', 'QToolBar',
            'QDialogButtonBox', 'QGraphicsTransform', 'QSplashScreen', 'QDirModel', 'QGraphicsView',
            'QSplitter', 'QToolBox', 'QGraphicsWidget', 'QSplitterHandle', 'QToolButton', 'QDockWidget',
            'QGridLayout', 'QStackedLayout', 'QGroupBox', 'QStackedWidget', 'QToolTip', 'QDoubleSpinBox',
            'QHBoxLayout', 'QTreeView', 'QHeaderView', 'QTreeWidget', 'QErrorMessage', 'QInputDialog',
            'QTreeWidgetItem', 'QStatusBar', 'QTreeWidgetItemIterator', 'QFileDialog', 'QItemDelegate',
            'QUndoCommand', 'QFileIconProvider', 'QItemEditorCreatorBase', 'QStyle', 'QUndoGroup',
            'QFileSystemModel', 'QItemEditorFactory', 'QStyleFactory', 'QUndoStack', 'QFocusFrame',
            'QStyleHintReturn', 'QUndoView', 'QFontComboBox', 'QKeyEventTransition',
            'QStyleHintReturnMask', 'QVBoxLayout', 'QFontDialog', 'QStyleHintReturnVariant',
            'QLCDNumber', 'QStyleOption', 'QWhatsThis', 'QLabel', 'QStyleOptionButton', 'QWidget',
            'QFormLayout', 'QLayout', 'QStyleOptionComboBox', 'QWidgetAction', 'QFrame', 'QLayoutItem',
            'QStyleOptionComplex', 'QWidgetItem', 'QLineEdit', 'QStyleOptionDockWidget', 'QWizard',
            'QGesture', 'QListView', 'QStyleOptionFocusRect', 'QGestureEvent', 'QListWidget', 'QStyleOptionFrame',
            'QWizardPage', 'QGestureRecognizer', 'QListWidgetItem', 'QStyleOptionGraphicsItem']

# Prefer PyQt4
_SUPPORTED_BACKEND = ['PyQt4', 'PySide', 'PyQt5']

for backend in _SUPPORTED_BACKEND:
    try:
        _QT_MODULE = import_module(backend)
        break
    except ImportError:
        pass

if _QT_MODULE is None:
    raise ImportError("No compatible Qt library found. Need one of: " + ", ".join(_SUPPORTED_BACKEND))

if _QT_MODULE.__name__ == 'PyQt4':
    import sip
    sip.setapi('QString', 2)
    sip.setapi('QVariant', 2)

    from PyQt4 import QtGui as Gui
    from PyQt4 import QtCore as Core
    from PyQt4 import Qt, uic

    Widgets = ModuleType('Widgets')
    for widget in _WIDGETS:
        setattr(Widgets, widget, getattr(Gui, widget))

    Signal = Core.pyqtSignal
    Slot = Core.pyqtSlot
    Property = Core.pyqtProperty

elif _QT_MODULE.__name__ == 'PyQt5':
    from PyQt5 import QtCore as Core
    from PyQt5 import QtGui as Gui
    from PyQt5 import QtWidgets
    from PyQt5 import Qt, uic

    Widgets = ModuleType('Widgets')
    for widget in _WIDGETS:
        setattr(Widgets, widget, getattr(QtWidgets, widget))

    Signal = Core.Signal
    Slot = Core.Slot
    Property = Core.Property

elif _QT_MODULE.__name__ == 'PySide':
    from _QT_MODULE.__name__ import QtGui as Gui
    from _QT_MODULE.__name__ import QtCore as Core
    from _QT_MODULE.__name__ import Qt, uic

    Widgets = ModuleType('Widgets')
    for widget in _WIDGETS:
        setattr(Widgets, widget, getattr(Gui, widget))

    Signal = Core.Signal
    Slot = Core.Slot
    Property = Core.Property

# Dark Magic to make fake modules for importing from
sys.modules[__name__ + '.Widgets'] = Widgets
sys.modules[__name__ + '.Core'] = Core
sys.modules[__name__ + '.Gui'] = Gui
sys.modules[__name__ + '.Qt'] = Qt
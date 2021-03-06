from tkinter import *
from tkinter import ttk


def get_scale(root):
	"""To display in high-dpi we need to grab the scale factor from OS"""
	
	import platform, traceback, subprocess
	# There is no solution on XP
	
	if platform.system() == "Windows" and platform.release() == "XP":
		return 1.0
	
	# Windows
	# https://github.com/eight04/ComicCrawler/issues/13#issuecomment-229367171
	try:
		from ctypes import windll
		user32 = windll.user32
		user32.SetProcessDPIAware()
		w = user32.GetSystemMetrics(0)
		return w / root.winfo_screenwidth()
	except ImportError:
		pass
	except Exception as e:
		traceback.print_exc()
	
	# GNome
	try:
		args = ["gsettings", "get", "org.gnome.desktop.interface", "scaling-factor"]
		with subprocess.Popen(args, stdout=subprocess.PIPE, universal_newlines=True) as p:
			return float(p.stdout.read().rpartition(" ")[-1])
	except Exception:
		traceback.print_exc()
	
	return 1.0

row1=20
class UIdraw:
	def __init__(self):
		# root
		self.root = Tk()
		self.root.title("Manga DLer - Odaimoko")
		self.mainframe = ttk.Frame(self.root)
		self.mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
		self.search_text = StringVar(self.mainframe)
		self.link_text = StringVar(self.mainframe)
		self.input_combo_text = StringVar(self.mainframe)
		
		self.inputlabel = ttk.Label(self.mainframe, text="输入书本id→")
		self.inputlabel.grid(column=10, row=row1)
		self.inputlink = ttk.Entry(self.mainframe, textvariable=self.link_text)
		self.inputlink.grid(column=20, row=row1)
		self.input_combo = ttk.Combobox(self.mainframe, textvariable=self.input_combo_text,
		                                state="readonly",width=10)
		self.input_combo.grid(column=25, row=row1)
		self.inputbtn = ttk.Button(self.mainframe, text="分析")
		self.inputbtn.grid(column=30, row=row1)
		
		self.inputlabel = ttk.Label(self.mainframe, text="搜本地书名↓")
		self.inputlabel.grid(column=10, row=30)
		self.searchlocal = ttk.Entry(self.mainframe, textvariable=self.search_text)
		self.searchlocal.grid(column=10, row=50)
		# 已下载过的书
		self.localbooks = Listbox(self.mainframe, height=10)
		self.localbooks.grid(column=10, row=100)
		# 每一话
		self.episode_list = Listbox(self.mainframe, height=10)
		self.episode_list.grid(column=20, row=100)
		# 配套进度
		self.episodes_dling = Listbox(self.mainframe, height=10)
		self.episodes_dling.grid(column=25,row=100)
		
		self.episodes_scrollbar = ttk.Scrollbar(self.mainframe, orient=VERTICAL, command=self.episode_list.yview)
		self.episodes_scrollbar.grid(column=30, row=100)
		self.episode_list.configure(yscrollcommand=self.episodes_scrollbar.set)


class EventBinder:
	pass


class MainUI(UIdraw):
	def __init__(self):
		UIdraw.__init__(self)
		self.root.mainloop()
		pass


if __name__ == '__main__':
	MainUI()

import fitz

doc = fitz.open(r"D:\Claude Code\Antigravity\Praveen\Home Planning\flat902_furniture_plan.svg")
page = doc[0]
pix = page.get_pixmap(matrix=fitz.Matrix(2,2))
pix.save(r"D:\Claude Code\Antigravity\Praveen\Home Planning\flat902_furniture_plan.png")
print("done", pix.width, pix.height)

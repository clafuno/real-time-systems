##Module: chronogram

import svgwrite

separation = 50
offset = 20
inc = 20
heigth = 10
tNum = 0
taskId = {}
fout = "chronogram.svg"

xmax = 0
ymax = 0
lines = 0
labels = []
taskIds = {}
palette = ["brown", "darkblue", "green", "orange", "aqua", "bisque",  "magenta", "lime", "blue", "yellow", "chocolate", "crimson", 
"sienna", "salmon", "fuchsia", "grey",  "lightgreen", "indigo", "darkolivegreen", "cadetblue", "purple","olive","darkmagenta","yellowgreen","darkkhaki","lightblue","lightcyan","magenta","darkred","violet","gray","slateblue", 
    "lightsteelblue", "mediumblue","navajowhite", "slategrey","violet", "tomato","darkslateblue", "mediumvioletred","forestgreen", "indianred","goldenrod", "dodgerblue","darkred"]
color = []
dwg = None

    
def chronoInit(nlines, width, fname):
    global xmax, ymax, lines, dwg

    lines = nlines
    xmax = width
    ymax = lines * separation
    fout = fname+".svg"
    for i in range(lines):
        labels.append("")
    dwg = svgwrite.Drawing(fout, profile='tiny')
    dwg.add(dwg.rect((offset, offset), size=(xmax, ymax), fill='whitesmoke'))
    
    xpos = 0
    while (xpos <= xmax):
        dwg.add(dwg.line((offset + xpos, offset), (offset + xpos, offset + ymax), stroke='grey', stroke_width=1).dasharray([3,3]))
        dwg.add(dwg.text(str(xpos), insert=(offset + xpos-3, 6+offset + ymax), font_size="6px"))
        xpos += inc
    

def chronoAddLine(nline, tag):
    global dwg
    labels[nline] = tag
    lpos = nline + 1
    dwg.add(dwg.text(labels[nline], insert=(0, lpos * separation)))
    dwg.add(dwg.line((offset, lpos * separation), (offset+ xmax, lpos * separation), stroke='black'))


def chronoAddExec(nline, start, end, task):
    global dwg, tNum

    if (taskIds.has_key(task)):
        ntsk = taskIds[task]
    else:
        taskIds[task] = tNum % len(palette)
        ntsk = tNum
        tNum += 1
    lpos = nline + 1
    dwg.add(dwg.rect((start + offset, (lpos * separation)-heigth), size=(end-start, heigth), fill=palette[ntsk]))


    
def chronoClose():
    xpos = offset 
    ypos = ymax + 30
    nt = 0
    for tsk in sorted(taskIds.keys()):
		    idx = taskIds[tsk]
		    dwg.add(dwg.text(tsk, insert=(xpos, ypos+7), font_size="6px"))
		    dwg.add(dwg.rect((xpos + 15, ypos), size=(10, heigth), fill=palette[idx]))
		    xpos = xpos + offset + 20
		    nt += 1
		    if (nt > 20):
		        ypos = ypos + 20
		        xpos = offset
		        nt = 0
    dwg.save()
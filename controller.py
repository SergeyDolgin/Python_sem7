import importer
import exp
import inp
import logg

def start():
    if inp.mod() == '1':
        info = inp.exp()
        exp.export(info)
        logg.log_info(info)
    elif inp.mod() == '2':
        info = inp.inpp()
        importer.impo(info)
        logg.log_info(info)
    else: 
        print('в программе только два режима работы')
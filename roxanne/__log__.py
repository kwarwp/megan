
{'date': 'Tue Sep 19 2023 12:25:19.833 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''
 module <string> line 12
  oceano = Cena(imagem).vai()
  ^
IndentationError: expected an indented block
'''},
{'date': 'Tue Sep 19 2023 12:25:40.141 GMt-0300 (Brasilia Standard Time) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 180
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 135
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 310
    return self._first_response(lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 282
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 299
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 4
    STYLE["width"] = 800
AttributeError: 'module' object has no attribute '__setitem__'
'''},
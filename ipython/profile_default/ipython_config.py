
from IPython.terminal.prompts import Prompts, Token

class MyPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [ ( Token.Prompt, "ipy> ",), ]

    def out_prompt_tokens(self, cli=None):
        return []

c.InteractiveShell.separate_in = ""
c.InteractiveShell.prompts_class = MyPrompt
c.InteractiveShell.autoindent = False


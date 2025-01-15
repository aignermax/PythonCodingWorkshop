# lsp_bad.py

class Bird:
    def fly(self):
        print("I am flying")

class Eagle(Bird):
    pass  # Eagle can fly, no problem

class Ostrich(Bird):
    """
    Ostrich cannot fly, so if we rely on fly(),
    it's going to break our expectations.
    """
    def fly(self):
        # Violates LSP: Ostrich can't really fly
        raise NotImplementedError("Ostrich cannot fly")

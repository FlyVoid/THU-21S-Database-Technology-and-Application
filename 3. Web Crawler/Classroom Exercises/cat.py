class Cat:
    def __init__(self):
        print('A cat comes here.')
    
    def __enter__(self):
        print('The cat stands in front of you.')
        return self
    
    def __exit__(self,exc_type,exc_val,exc_tb):
        print('The Cat is gone.')
    
    def meow(self):
        print('Meow')

if __name__=='__main__':
    with Cat() as cat:
        cat.meow()
        
        
        
        
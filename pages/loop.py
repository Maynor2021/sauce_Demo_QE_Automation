
arr=[1,2,3,4,5]
class LoopPage:
    def __init__(self, page):
        self.page = page
    
    def log(self, message):
        self.page.evaluate(f"console.log('{message}')")
        print(message)
        
        
        
def loop(arr):
    for i in arr:
        print(i)


logi=LoopPage('page object')

print("Ejecutando loop...")
print (logi.log("Iniciando loop..."))

       

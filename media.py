
# Part-A: create class Tv
class Tv:   #base class
    channel = 1
    ledPrice = "$2000"
    ledInches = "65`"
    ledScreenThickness = "Less than 1 inch"
    ledEnergyUsage = "Less"
    ledBacklight = "Yes"
    ledLifeSpan = "100,000 hours"

    plasmaPrice = "$1000"
    plasmaInches = "55`"
    plasmaScreenThickness = "Minimum 1.2 inch"
    plasmaEnergyUsage = "More"
    plasmaBacklight = "No"
    plasmaLifeSpan = "20,000 to 60,000 hours"

    onOffStatus = 0
    volume = 50

#Constructor parameter for brand
    def __init__(self):
        self.name = "Sony"
    def tvBrand(self):
        return self.name

# Method to increase the volume
    def increaseVolume(self, adjVolume):
        if (adjVolume > 50 and adjVolume <= 100):
            self.volume = adjVolume
            print("The volume is increased from 50 to",self.volume)
        
        if (adjVolume == 50):
            self.volume = adjVolume
            print("The volume entered is default volume", self.volume)
            
        if (adjVolume < 0 or adjVolume > 100):
            self.volume = 50
            print("Volume is out of range it sets to default value", self.volume)
            
#Method to decrease the volume
    def decreaseVolume(self, adjVolume):
        if (adjVolume >= 0 and adjVolume < 50):
            self.volume = adjVolume
            print("The volume is decreased from 50 to", self.volume)
            

#Method to set the channel
    def setChannel(self, adjChannel):
        if (adjChannel > 1 and adjChannel <= 50):
            self.channel = adjChannel
            print("The channel is increased from default 1 to", self.channel)
            
        if(adjChannel == 1):
            self.channel = adjChannel
            print("Channel entered is default channel",self.channel)
           
        if(adjChannel < 1 or adjChannel > 50):
            self.channel = 1
            print("The channel is out of range and stay at default current channel", self.channel)

#Method to print TV status
    def tvStatus(self, adjVolume, adjChannel):

        if (adjVolume < 0 and adjChannel < 1): #Lower invalid limits for volume and channel
            self.volume = 50
            self.channel = 1
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        elif(adjVolume > 100 and adjChannel > 50): #Higher invalid limits for volume and channel
            self.volume = 50
            self.channel = 1
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        elif(adjVolume < 0 and adjChannel >=1 and adjChannel <= 50): #Lower invalid limit volume and valid channel
            self.volume = 50
            self.channel = adjChannel
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        elif(adjVolume >100 and adjChannel >=1 and adjChannel <= 50): #Higher invalid limit volume and valid channel
            self.volume = 50
            self.channel = adjChannel
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        elif(adjChannel < 1 and adjVolume >=0 and adjVolume <= 100): #Lower invalid limit channel and valid volume
            self.channel = 1
            self.volume = adjVolume
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        elif(adjChannel > 50 and adjVolume >=0 and adjVolume <= 100): #Higher invalid limit channel abd valid volume
            self.channel = 1
            self.volume = adjVolume
            print("TV status like:", self.tvBrand(), "at channel", self.channel,",", "volume",self.volume)
        else:
            print("TV status like:", self.tvBrand(), "at channel", adjChannel,",", "volume",adjVolume)
            
  
#Method to reset TV
    def reset(self, res):
        if (res == "y"):
            self.volume = 50
            self.channel = 1
            print("The volume is reset to", self.volume)
            print("The channel is reset to", self.channel)

#Get input from user
adjVolume = int(input("Please enter the volume level 0-100 default is 50:"))
adjChannel = int(input("Please enter the Channel between 1-50:"))
#create object or instance of class
e = Tv()
e.increaseVolume(adjVolume)
e.decreaseVolume(adjVolume)
e.setChannel(adjChannel)
e.tvStatus(adjVolume, adjChannel)

# Reset the TV
res = input("Please enter Y or N to reset the TV:")
res = res.lower()
e.reset(res)

#Part B: Create LedTv and PlasmaTv class and inherit Tv class

class LedTv(Tv): #child class
    model = "LED TV Details:"

f = LedTv()
print("\n")
print(f.model)
print("==============")
print("Price:",f.ledPrice)
print("Inches:",f.ledInches)
print("Screen Thickness:",f.ledScreenThickness)
print("Energy Usage:",f.ledEnergyUsage)
print("Back Light:",f.ledBacklight)
print("Life Span:",f.ledLifeSpan)

class PlasmaTv(Tv): #child class
    model = "Plasma Tv Details:"

g = PlasmaTv()
print("\n")
print(g.model)
print("=================")
print("Price:",g.plasmaPrice)
print("Inches:",g.plasmaInches)
print("Screen Thickness:",g.plasmaScreenThickness)
print("Energy Usage:",g.plasmaEnergyUsage)
print("Back Light:",g.plasmaBacklight)
print("Life Span:",g.plasmaLifeSpan)
    
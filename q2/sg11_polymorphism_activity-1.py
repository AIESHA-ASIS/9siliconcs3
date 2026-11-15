class Patient():
  def __init__(self, name: str, bill_amount: float):
    self.__name = name
    self.__bill_amount = bill_amount

  def get_name(self):
    return f"Patient Name: {self.__name}"

  def set_name(self, name):
    self.__name = name 

  def get_bill_amount(self):
    return self.__bill_amount

  def set_bill_amount(bill_amount):
    self.__bill_amount = bill_amount

  def calculate_bill(self):
    return self.get_bill_amount()
    
  def display_patient_type(self):
    return "Patient Type: Regular patient"
  
class SeniorPatient(Patient):
  def calculate_bill(self):
    return self.get_bill_amount() * 0.80

  def display_patient_type(self):
    return "Patient type: Senior Citizen"

class PhilHealthPatient(Patient):
  def calculate_bill(self):
    return self.get_bill_amount() * 0.85

  def display_patient_type(self):
    return "Patient type: PhilHealth Member"


def main(): 
  print("Hospital Billing System")
  print("-----------------------")

  patients = [
    Patient("Juan Dela Cruz", 15000.00),
    SeniorPatient("Maria Santos", 15000.00),
    PhilHealthPatient("Pedro Reyes", 15000.00)
  ]

  for i in patients:
    print(f"{i.get_name()}")
    i.display_patient_type()
    print(f"Original Bill: ₱{i.get_bill_amount():,.2f}")
    print(f"Final Bill: ₱{i.calculate_bill():,.2f}\n")
    
          
    
main()

  
  
class Company:
    def __init__(self, name, head):
        self.name = name
        self.head = head
    
    def get_info(self):
        return f"Company:{self.name}|Head:{self.head}"
    
class ITCompany(Company):
    def __init__(self, name, head,services):
        super().__init__(name, head)
        self.services = services
    
    def get_services(self):
        return self.services
            
comp_name, comp_head, comp_services = company_info
it_company_obj = ITCompany(name=comp_name, head=comp_head, services=comp_services)
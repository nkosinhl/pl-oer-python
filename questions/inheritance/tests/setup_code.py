import random

def generate_company_tuple():
    comp_heads = ["Maxwell Sterling","Penelope Stone","Harrison Blackwood","Seraphina Wilde","Jasper North","Arabella Raven","Felix Hawthorne","Imogen Frost","Atticus Silver","Ophelia Nightshade"]
    comp_services = ["Network Infrastructure Management", "System Administration", "Cybersecurity Services", "Software Development", "Help Desk and User Support", "Database Management", "Cloud Computing Services", "IT Project Management", "IT Consultancy", "Data Backup and Recovery", "Server Maintenance and Monitoring", "Mobile Device Management (MDM)", "Virtualization Services", "IT Training and Workshops", "Hardware Procurement and Maintenance", "Network Security Audits", "Software Licensing Management", "IT Asset Management", "VoIP (Voice over Internet Protocol) Implementation", "Incident Response and Resolution"]
    comp_names = ["QuantumTech Solutions", "CodeCraft Innovations", "DataPulse Systems", "CyberNex Solutions", "ByteWave Technologies", "InnovIT Labs", "LogicSphere Systems", "InfraSync Solutions", "TechnoFusion Services", "DigitalVibe Technologies"]

    comp_name = random.choice(comp_names)
    comp_head = random.choice(comp_heads)
    comp_services = random.sample(comp_services, 4)
    return (comp_name, comp_head, comp_services)

company_info = generate_company_tuple()
from django.db import models

# Create your models here.

class Industry(models.Model):
    INDUSTRY_CHOICES = [
        ('ai_ml', 'AI/ML'),
        ('ar_vr', 'AR/VR'),
        ('agritech', 'Agritech'),
        ('b2b', 'B2B'),
        ('b2c', 'B2C'),
        ('biotech', 'Biotech'),
        ('cleantech', 'CleanTech/Sustainability'),
        ('edtech', 'EdTech'),
        ('ecommerce', 'E-Commerce'),
        ('fintech', 'Fintech'),
        ('hardware', 'Hardware'),
        ('healthtech', 'Healthtech'),
        ('iot', 'IoT'),
        ('marketplace', 'Marketplace'),
        ('media_content', 'Media & Content'),
        ('mobility_logistics', 'Mobility/Logistics'),
        ('social_impact', 'Social Impact'),
    ]
    
    name = models.CharField(max_length=50, choices=INDUSTRY_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_name_display()

class Skill(models.Model):
    SKILL_CHOICES = [
        # Technical Skills
        ('python', 'Python'),
        ('java', 'Java'),
        ('rust', 'Rust'),
        ('sql', 'SQL'),
        ('web_development', 'Web Development'),
        ('app_development', 'App Development'),
        ('machine_learning', 'Machine Learning'),
        ('cloud_platforms', 'Cloud Platforms'),
        ('ui_ux_design', 'UI/UX Design'),
        ('tech_others', 'Others (Technical)'),
        # Business/Finance Skills
        ('financial_modeling', 'Financial Modeling'),
        ('budgeting_forecasting', 'Budgeting & Forecasting'),
        ('sales_lead_generation', 'Sales & Lead Generation'),
        ('marketing_analytics', 'Marketing Analytics'),
        ('fundraising_negotiation', 'Fundraising & Negotiation'),
        ('data_analysis', 'Data Analysis'),
        ('business_others', 'Others (Business)'),
    ]
    
    name = models.CharField(max_length=50, choices=SKILL_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_name_display()

class Role(models.Model):
    ROLE_CHOICES = [
        ('co_founder_general', 'Co-Founder (General)'),
        ('ceo_business_lead', 'CEO/Business Lead'),
        ('cto_technical_lead', 'CTO/Technical Lead'),
        ('cmo_marketing_lead', 'CMO/Marketing Lead'),
        ('cfo_finance_lead', 'CFO/Finance Lead'),
        ('ai_ml_engineer', 'AI/ML Engineer'),
        ('cloud_engineer', 'Cloud Engineer'),
        ('app_developer', 'App Developer'),
        ('web_developer', 'Web Developer'),
        ('ui_ux_designer', 'UI/UX Designer'),
    ]
    
    name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)
    
    def __str__(self):
        return self.get_name_display()

class Project(models.Model):
    industries = models.ManyToManyField(Industry, blank=True)
    roles = models.ManyToManyField(Role, blank=True)

class Profile(models.Model):
    industries = models.ManyToManyField(Industry, blank=True)
    skills = models.ManyToManyField(Skill, blank=True)

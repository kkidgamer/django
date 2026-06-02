# employees/models.py
from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    """
    Defines the database schema blueprint for storing corporate employee profiles.
    """
    # ADDED RELATIONSHIP: Simple link to the Department model
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    # 1. Plain Text Fields
    first_name = models.CharField(max_length=100, help_text="The employee's first or given name.")
    last_name = models.CharField(max_length=100, help_text="The employee's family or legal surname.")
    email = models.EmailField(unique=True, help_text="Unique corporate email address contact.")
    
    # 2. Long-Form Text Blocks
    biography = models.TextField(blank=True, help_text="Optional background notes or experience history.")
    
    # 3. Numeric & Financial Fields
    salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        default=0.00,
        help_text="Base annual compensation amount."
    )
    
    # 4. Role Status Configurations using standardized text choice enums
    class RoleChoices(models.TextChoices):
        TRAINEE = 'TR', 'Trainee'
        DEVELOPER = 'DV', 'Developer'
        MANAGER = 'MG', 'Manager'
        EXECUTIVE = 'EX', 'Executive'
        
    role = models.CharField(
        max_length=2,
        choices=RoleChoices.choices,
        default=RoleChoices.TRAINEE,
        help_text="Current internal organizational position assignment."
    )
    
    # 5. Timestamp Tracking Fields
    date_joined = models.DateTimeField(auto_now_add=True, help_text="Timestamp logging when profile was created.")
    last_updated = models.DateTimeField(auto_now=True, help_text="Timestamp auto-updating on every save operation.")

    class Meta:
        # Sort queries by creation timestamp in descending order (newest profiles first) by default
        ordering = ['-date_joined']
        verbose_name = "Employee Profile"
        verbose_name_plural = "Employee Profiles"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.get_role_display()})"

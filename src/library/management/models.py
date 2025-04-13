from django.db import models
from library.models import Book, Publisher
from users.models import LibraryUser

class LibraryBranch(models.Model):
    """Model for physical library locations"""
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    opening_hours = models.TextField()
    
    def __str__(self):
        return self.name

class BookCopy(models.Model):
    """Model for individual physical copies of books"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='copies')
    branch = models.ForeignKey(LibraryBranch, on_delete=models.CASCADE, related_name='inventory')

    CONDITION_CHOICE = [
        ('new', 'New ✨'),
        ('good', 'Good 👍'),
        ('fair', 'Fair 👌'),
        ('poor', 'Poor 👎'),
        ('damaged', 'Damaged 💔'),
    ]

    condition = models.CharField(max_length=10, choice=CONDITION_CHOICE, default='good')
    acquisition_date = models.DateField()
    inventory_number = models.CharField(max_length=50, unique=True)
    is_available = models.BooleanField(default=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Copy {self.inventory_number} of {self.book.title}"

class BookLoan(models.Model):
    """Model for book borrowing records"""
    copy = models.ForeignKey(BookCopy, on_delete=models.CASCADE, related_name='loans')
    checkout_date = models.DateField()
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)

    STATUS_CHOICE = [
        ('active', 'Active 📚'),
        ('returned', 'Returned ✅'),
        ('overdue', 'Overdue ⚠️'),
        ('lost', 'Lost ❌'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default='active')

    def __str__(self):
        return f"{self.copy.book.title} borrowed by {self.borrower.username}"

class Reservation(models.Model):
    """Model for book reservations"""
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey(LibraryUser, on_delete=models.CASCADE, related_name='reservations')
    branch = models.ForeignKey(LibraryBranch, on_delete=models.CASCADE, related_name='reservations')
    request_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending ⏳'),
        ('ready', 'Ready for Pickup ✅'),
        ('fulfilled', 'Fulfilled 📚'),
        ('cancelled', 'Cancelled ❌'),
    ], default='pending')
    
    def __str__(self):
        return f"Reservation of {self.book.title} by {self.user.username}"
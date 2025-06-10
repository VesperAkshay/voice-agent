"""
Grievance registration tool for Indian Grievance Resolver.
"""

from typing import Dict, Any, Optional
from .ticket_manager import ticket_manager

def register_grievance(
    name: str,
    contact: str,
    category: str,
    description: str,
    language: str,
    location: str,
    priority: str
) -> dict:
    """
    Register a new grievance.
    
    Args:
        name (str): Name of the person registering the grievance
        contact (str): Contact information (email/phone)
        category (str): Category of the grievance (e.g., 'Housing', 'Education', 'Healthcare')
        description (str): Detailed description of the grievance
        language (str): Preferred language for communication (default: 'en' for English)
        location (str): Location/address related to the grievance
        priority (str): Priority level (Low/Medium/High)
    
    Returns:
        dict: Information about the registered grievance
    """
    try:
        # Set default values for optional parameters
        language = language or 'en'
        priority = priority or 'Medium'
        
        # Create a new ticket using the ticket manager
        ticket = ticket_manager.create_ticket(
            name=name,
            contact=contact,
            category=category,
            description=description,
            language=language,
            location=location,
            priority=priority,
            # Include any additional fields that might be needed
            original_request={
                'name': name,
                'contact': contact,
                'category': category,
                'description': description,
                'language': language,
                'location': location,
                'priority': priority
            }
        )
        
        return {
            'status': 'success',
            'message': 'Grievance registered successfully',
            'ticket_id': ticket['ticket_id'],
            'tracking_number': f"GRV{ticket['ticket_id']:06d}",
            'status': ticket['status'],
            'created_at': ticket['created_at']
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to register grievance: {str(e)}'
        }

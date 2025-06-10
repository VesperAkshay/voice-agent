"""
Grievance status check tool for Indian Grievance Resolver.
"""

from typing import Dict, Any
from .ticket_manager import ticket_manager

def check_status(ticket_id: int) -> Dict[str, Any]:
    """
    Check the status of a registered grievance ticket.
    
    Args:
        ticket_id (int): The ID of the ticket to check
        
    Returns:
        dict: Status information about the ticket
    """
    try:
        ticket = ticket_manager.get_ticket(ticket_id)
        
        if not ticket:
            return {
                'status': 'error',
                'message': f'No ticket found with ID: {ticket_id}'
            }
            
        return {
            'status': 'success',
            'ticket_id': ticket['ticket_id'],
            'tracking_number': f"GRV{ticket['ticket_id']:06d}",
            'status': ticket['status'],
            'resolved': ticket.get('resolved', False),
            'category': ticket.get('category', 'Not specified'),
            'description': ticket.get('description', 'No description provided'),
            'created_at': ticket.get('created_at'),
            'updated_at': ticket.get('updated_at')
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to check ticket status: {str(e)}'
        }

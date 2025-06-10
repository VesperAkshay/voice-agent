"""
Ticket update tool for Indian Grievance Resolver.
"""

from typing import Dict, Any, Optional, Union
from .ticket_manager import ticket_manager

def update_ticket(
    ticket_id: int,
    status: str,
    resolved: bool,
    resolution_notes: str
) -> Dict[str, Any]:
    """
    Update a ticket's status or resolution status.
    
    Args:
        ticket_id (int): The ID of the ticket to update
        status (str, optional): New status (e.g., 'In Progress', 'Resolved', 'Closed')
        resolved (bool, optional): Whether the issue is resolved
        resolution_notes (str, optional): Notes about the resolution
        
    Returns:
        dict: Information about the updated ticket or error message
    """
    try:
        # Set default values if not provided
        status = status or 'Open'
        resolved = resolved or False
        resolution_notes = resolution_notes or ''
        
        # Get the current ticket to verify it exists
        ticket = ticket_manager.get_ticket(ticket_id)
        if not ticket:
            return {
                'status': 'error',
                'message': f'No ticket found with ID: {ticket_id}'
            }
        
        # Update the ticket status if provided
        if status is not None:
            success = ticket_manager.update_ticket_status(
                ticket_id=ticket_id,
                status=status,
                resolved=resolved
            )
            if not success:
                return {
                    'status': 'error',
                    'message': 'Failed to update ticket status'
                }
        
        # Get the updated ticket
        updated_ticket = ticket_manager.get_ticket(ticket_id)
        
        # Add resolution notes if provided
        if resolution_notes is not None:
            if 'resolution_notes' not in updated_ticket:
                updated_ticket['resolution_notes'] = []
            updated_ticket['resolution_notes'].append({
                'timestamp': updated_ticket['updated_at'],
                'notes': resolution_notes
            })
            # Save the ticket with resolution notes
            ticket_manager._save_tickets()
        
        return {
            'status': 'success',
            'message': 'Ticket updated successfully',
            'ticket_id': updated_ticket['ticket_id'],
            'tracking_number': f"GRV{updated_ticket['ticket_id']:06d}",
            'status': updated_ticket['status'],
            'resolved': updated_ticket.get('resolved', False),
            'updated_at': updated_ticket['updated_at']
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to update ticket: {str(e)}'
        }

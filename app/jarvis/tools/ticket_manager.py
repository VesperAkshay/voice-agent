"""
Ticket management system for handling grievance tickets.
"""

from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Optional, Any, Union

class TicketManager:
    def __init__(self, db_path: str = 'grievances.json'):
        """
        Initialize the TicketManager with a JSON database file.
        
        Args:
            db_path (str): Path to the JSON database file
        """
        self.db_path = Path(db_path)
        self.tickets = self._load_tickets()
    
    def _load_tickets(self) -> List[Dict[str, Any]]:
        """Load tickets from the JSON file."""
        if not self.db_path.exists():
            return []
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def _save_tickets(self) -> None:
        """Save tickets to the JSON file."""
        with open(self.db_path, 'w', encoding='utf-8') as f:
            json.dump(self.tickets, f, indent=2, ensure_ascii=False)
    
    def create_ticket(
        self,
        name: str,
        contact: str,
        category: str,
        description: str,
        language: str = 'en',
        location: Optional[str] = None,
        priority: str = 'Medium',
        **extra_data: Any
    ) -> Dict[str, Any]:
        """
        Create a new ticket.
        
        Args:
            **ticket_data: Ticket details including:
                - name: Name of the person
                - contact: Contact information
                - category: Category of the issue
                - description: Detailed description
                - language: Preferred language (default: 'en')
                - location: Location related to the issue (optional)
                - priority: Priority level (Low/Medium/High, default: 'Medium')
        
        Returns:
            dict: Created ticket with ID and status
        """
        ticket_id = len(self.tickets) + 1
        timestamp = datetime.now().isoformat()
        
        ticket = {
            'ticket_id': ticket_id,
            'name': name,
            'contact': contact,
            'category': category,
            'description': description,
            'language': language,
            'location': location,
            'priority': priority,
            'status': 'Open',
            'created_at': timestamp,
            'updated_at': timestamp,
            'resolved': False,
            **extra_data
        }
        
        self.tickets.append(ticket)
        self._save_tickets()
        return ticket
    
    def get_ticket(self, ticket_id: int) -> Optional[Dict[str, Any]]:
        """
        Get a ticket by ID.
        
        Args:
            ticket_id (int): The ticket ID to look up
            
        Returns:
            Optional[dict]: The ticket if found, None otherwise
        """
        for ticket in self.tickets:
            if ticket.get('ticket_id') == ticket_id:
                return ticket
        return None
    
    def update_ticket_status(self, ticket_id: int, status: str, resolved: bool = None) -> bool:
        """
        Update a ticket's status.
        
        Args:
            ticket_id (int): The ticket ID to update
            status (str): New status (e.g., 'In Progress', 'Resolved', 'Closed')
            resolved (bool, optional): Whether the issue is resolved
            
        Returns:
            bool: True if update was successful, False otherwise
        """
        for ticket in self.tickets:
            if ticket.get('ticket_id') == ticket_id:
                ticket['status'] = status
                ticket['updated_at'] = datetime.now().isoformat()
                if resolved is not None:
                    ticket['resolved'] = resolved
                self._save_tickets()
                return True
        return False
    
    def get_all_tickets(self) -> List[Dict[str, Any]]:
        """
        Get all tickets.
        
        Returns:
            List[dict]: List of all tickets
        """
        return self.tickets

# Create a singleton instance
ticket_manager = TicketManager()

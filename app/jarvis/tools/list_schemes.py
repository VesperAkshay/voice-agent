"""
List available government schemes for Indian Grievance Resolver.
"""

from typing import Dict, List, Any, Optional

SCHEMES = {
    'pm_kisan': {
        'name': 'PM KISAN',
        'description': 'Income support scheme for farmers',
        'category': 'Agriculture',
        'ministry': 'Ministry of Agriculture & Farmers Welfare'
    },
    'pmay_urban': {
        'name': 'Pradhan Mantri Awas Yojana (Urban)',
        'description': 'Housing for All by 2022',
        'category': 'Housing',
        'ministry': 'Ministry of Housing and Urban Affairs'
    },
    'pmjjby': {
        'name': 'Pradhan Mantri Jeevan Jyoti Bima Yojana',
        'description': 'Life insurance coverage',
        'category': 'Insurance',
        'ministry': 'Ministry of Finance'
    },
    'pmsym': {
        'name': 'Pradhan Mantri Shram Yogi Maan-dhan',
        'description': 'Pension scheme for unorganized sector workers',
        'category': 'Pension',
        'ministry': 'Ministry of Labour and Employment'
    },
    'pmuy': {
        'name': 'Pradhan Mantri Ujjwala Yojana',
        'description': 'LPG connections for women from below poverty line families',
        'category': 'Energy',
        'ministry': 'Ministry of Petroleum and Natural Gas'
    },
    'pmjdy': {
        'name': 'Pradhan Mantri Jan Dhan Yojana',
        'description': 'Financial inclusion program',
        'category': 'Banking',
        'ministry': 'Ministry of Finance'
    }
}

def list_schemes(category: str) -> Dict[str, Any]:
    """
    List all available government schemes, optionally filtered by category.
    
    Args:
        category (str, optional): Filter schemes by category (e.g., 'Agriculture', 'Housing')
        
    Returns:
        dict: Dictionary containing the list of matching schemes
    """
    try:
        # If category is empty string, show all schemes
        if not category or category.lower() == 'all':
            schemes_list = list(SCHEMES.values())
            return {
                'status': 'success',
                'count': len(schemes_list),
                'schemes': schemes_list,
                'message': f'Found {len(schemes_list)} available schemes'
            }
            
        # Filter by category if specified
        filtered_schemes = {
            scheme_id: scheme for scheme_id, scheme in SCHEMES.items()
            if category.lower() in scheme['category'].lower()
        }
        schemes_list = list(filtered_schemes.values())
        message = f"Found {len(schemes_list)} scheme(s) in category '{category}'"
        
        return {
            'status': 'success',
            'count': len(schemes_list),
            'schemes': schemes_list,
            'message': message
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to list schemes: {str(e)}',
            'schemes': []
        }

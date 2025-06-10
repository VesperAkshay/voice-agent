"""
Get detailed information about a specific government scheme.
"""

from typing import Dict, Any, Optional

SCHEME_DETAILS = {
    'pm_kisan': {
        'name': 'PM KISAN',
        'full_name': 'Pradhan Mantri Kisan Samman Nidhi',
        'description': 'Income support scheme for farmers',
        'category': 'Agriculture',
        'ministry': 'Ministry of Agriculture & Farmers Welfare',
        'benefits': '₹6,000 per year in three equal installments of ₹2,000 every four months',
        'eligibility': [
            'Small and marginal farmers with cultivable landholding',
            'All farmer families in the country irrespective of the size of their land holdings',
            'Farmer families should have a valid Aadhaar number',
            'Certain categories of higher economic status are excluded'
        ],
        'documents_required': [
            'Aadhaar Card',
            'Land Records',
            'Bank Account Details',
            'Identity Proof',
            'Citizenship Certificate'
        ],
        'how_to_apply': [
            'Visit the official PM-KISAN portal (https://pmkisan.gov.in/)',
            'Click on "New Farmer Registration"',
            'Fill in the required details',
            'Upload necessary documents',
            'Submit the application',
            'Application can also be submitted through Common Service Centres (CSCs)'
        ],
        'helpline': '011-23381092, 23382401',
        'website': 'https://pmkisan.gov.in/'
    },
    'pmay_urban': {
        'name': 'PMAY-U',
        'full_name': 'Pradhan Mantri Awas Yojana - Urban',
        'description': 'Housing for All by 2022 mission',
        'category': 'Housing',
        'ministry': 'Ministry of Housing and Urban Affairs',
        'benefits': 'Interest subsidy on home loans up to ₹2.67 lakh',
        'eligibility': [
            'Economically Weaker Section (EWS) with annual income up to ₹3 lakh',
            'Lower Income Group (LIG) with annual income between ₹3-6 lakh',
            'Middle Income Group (MIG) with annual income between ₹6-18 lakh',
            'Beneficiary family should not own a pucca house in his/her name or any family member'
        ],
        'documents_required': [
            'Aadhaar Card',
            'Income Certificate',
            'Address Proof',
            'Property Documents (if applicable)',
            'Bank Account Details',
            'Affidavit for not owning a pucca house'
        ],
        'how_to_apply': [
            'Visit the PMAY-U website (https://pmaymis.gov.in/)',
            'Click on "Citizen Assessment" and select your category',
            'Fill the application form with required details',
            'Upload necessary documents',
            'Submit the application',
            'Note down the application reference number for future reference'
        ],
        'helpline': '1800-11-6163',
        'website': 'https://pmaymis.gov.in/'
    },
    'pmjjby': {
        'name': 'PMJJBY',
        'full_name': 'Pradhan Mantri Jeevan Jyoti Bima Yojana',
        'description': 'Life insurance coverage at affordable premium',
        'category': 'Insurance',
        'ministry': 'Ministry of Finance',
        'benefits': '₹2 lakh life cover at ₹330/year premium',
        'eligibility': [
            'Age group: 18-50 years',
            'Should have a savings bank account',
            'Should give consent to auto-debit of premium'
        ],
        'documents_required': [
            'Aadhaar Card',
            'Bank Account Details',
            'Nominee Details'
        ],
        'how_to_apply': [
            'Contact your bank where you have a savings account',
            'Fill up the enrollment form',
            'Provide Aadhaar number and other details',
            'Give consent for auto-debit of premium',
            'The premium will be automatically debited from your account'
        ],
        'helpline': '1800-180-1111',
        'website': 'https://www.jansuraksha.gov.in/'
    },
    'pmsym': {
        'name': 'PMSYM',
        'full_name': 'Pradhan Mantri Shram Yogi Maan-dhan',
        'description': 'Pension scheme for unorganized sector workers',
        'category': 'Pension',
        'ministry': 'Ministry of Labour and Employment',
        'benefits': 'Minimum assured pension of ₹3,000 per month after attaining 60 years of age',
        'eligibility': [
            'Unorganized workers between 18-40 years of age',
            'Monthly income up to ₹15,000',
            'Should have a savings bank account and Aadhaar number',
            'Should not be covered under New Pension Scheme (NPS), ESIC, EPFO, etc.'
        ],
        'documents_required': [
            'Aadhaar Card',
            'Savings Bank Account with IFSC',
            'Mobile Number linked with Aadhaar',
            'Income Certificate (if required)'
        ],
        'how_to_apply': [
            'Visit the nearest Common Service Centre (CSC)',
            'Provide Aadhaar number and savings bank account number',
            'The Village Level Entrepreneur (VLE) will verify your details',
            'Pay the monthly contribution amount',
            'You will receive a Shram Yogi Card with unique Shram Yogi Pension Account Number (SPAN)'
        ],
        'helpline': '1800-267-6888',
        'website': 'https://maandhan.in/'
    }
}

def get_scheme_details(scheme_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific government scheme.
    
    Args:
        scheme_id (str): The ID of the scheme (e.g., 'pm_kisan', 'pmay_urban')
        
    Returns:
        dict: Detailed information about the requested scheme
    """
    try:
        scheme = SCHEME_DETAILS.get(scheme_id.lower())
        
        if not scheme:
            return {
                'status': 'error',
                'message': f'Scheme with ID {scheme_id} not found'
            }
            
        return {
            'status': 'success',
            'scheme': scheme
        }
        
    except Exception as e:
        return {
            'status': 'error',
            'message': f'Failed to get scheme details: {str(e)}'
        }

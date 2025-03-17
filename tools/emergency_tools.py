from datetime import datetime
from typing import Dict, List, Any, Optional


def assess_medical_urgency(symptoms: str, medical_history: Optional[str] = None) -> Dict[str, Any]:
    """
    Assess the urgency level of a medical situation based on symptoms and history.
    
    Args:
        symptoms: Description of current symptoms
        medical_history: Optional medical history information
        
    Returns:
        A dictionary with urgency assessment results
    """
    urgent_keywords = ["chest pain", "difficulty breathing", "unconscious", "severe bleeding", 
                      "stroke", "heart attack", "severe allergic", "anaphylaxis"]
    
    urgency_level = "ROUTINE"
    if any(keyword in symptoms.lower() for keyword in urgent_keywords):
        urgency_level = "CRITICAL"
    elif "pain" in symptoms.lower() or "fever" in symptoms.lower():
        urgency_level = "URGENT"
        
    return {
        "urgency_level": urgency_level,
        "assessment_time": datetime.now().isoformat(),
        "requires_evacuation": urgency_level == "CRITICAL",
        "recommendations": f"Based on symptoms, this appears to be a {urgency_level.lower()} situation."
    }


def check_travel_advisory(country: str) -> Dict[str, Any]:
    """
    Check current travel advisories for a specific country.
    
    Args:
        country: The country to check advisories for
        
    Returns:
        Dictionary with advisory information
    """
    advisories = {
        "ukraine": {"level": "DO NOT TRAVEL", "risks": ["armed conflict", "civil unrest"]},
        "haiti": {"level": "DO NOT TRAVEL", "risks": ["kidnapping", "civil unrest"]},
        "afghanistan": {"level": "DO NOT TRAVEL", "risks": ["terrorism", "kidnapping"]},
        "japan": {"level": "EXERCISE NORMAL PRECAUTIONS", "risks": []},
        "italy": {"level": "EXERCISE NORMAL PRECAUTIONS", "risks": []},
        "egypt": {"level": "EXERCISE INCREASED CAUTION", "risks": ["terrorism"]},
        "mexico": {"level": "EXERCISE INCREASED CAUTION", "risks": ["crime", "kidnapping"]},
        "india": {"level": "EXERCISE INCREASED CAUTION", "risks": ["crime", "terrorism"]},
    }
    
    country_lower = country.lower()
    if country_lower in advisories:
        result = {
            "country": country,
            "advisory_level": advisories[country_lower]["level"],
            "risks": advisories[country_lower]["risks"],
            "as_of_date": datetime.now().strftime("%Y-%m-%d")
        }
        
    else:
        result = {
            "country": country,
            "advisory_level": "INFORMATION NOT AVAILABLE",
            "risks": [],
            "as_of_date": datetime.now().strftime("%Y-%m-%d")
        }
    
    return result


def find_emergency_accommodation(location: str, num_people: int, special_needs: Optional[str] = None) -> Dict[str, Any]:
    """
    Find emergency accommodation options in the specified location.
    
    Args:
        location: City or region where accommodation is needed
        num_people: Number of people needing accommodation
        special_needs: Any special requirements or accessibility needs
        
    Returns:
        Dictionary with accommodation options
    """
    options = [
        {
            "name": f"Emergency Shelter in {location}",
            "type": "Shelter",
            "capacity": "Large groups",
            "address": f"Main Emergency Center, {location}",
            "contact": "emergency@example.org"
        },
        {
            "name": f"Hotel Rapid Response in {location}",
            "type": "Hotel",
            "capacity": f"Can accommodate {num_people} people",
            "address": f"123 Safety St, {location}",
            "contact": "reservations@hotelrapidresponse.example.com"
        }
    ]
    
    if special_needs:
        options.append({
            "name": f"Accessible Haven in {location}",
            "type": "Specialized Facility",
            "capacity": "Limited but available",
            "address": f"456 Care Avenue, {location}",
            "notes": f"Equipped for {special_needs}",
            "contact": "access@haven.example.org"
        })
        
    return {
        "location": location,
        "available_options": options,
        "booking_instructions": "Contact the preferred option directly or reply with your selection for assistance."
    }


def check_visa_requirements(citizenship: str, destination: str, purpose: str) -> Dict[str, Any]:
    """
    Check emergency visa requirements and procedures.
    
    Args:
        citizenship: Country of citizenship
        destination: Destination country
        purpose: Purpose of travel (medical, evacuation, etc.)
        
    Returns:
        Dictionary with visa requirement information
    """
    if purpose.lower() == "medical":
        return {
            "required": True,
            "emergency_procedure_available": True,
            "documentation_needed": [
                "Passport valid for 6 months",
                "Doctor's letter stating medical necessity",
                "Proof of funds or insurance",
                "Emergency visa application form"
            ],
            "processing_time": "24-48 hours for emergency medical cases",
            "contact": f"{destination.title()} Embassy Emergency Line: +1-555-EMERGENCY"
        }
    elif purpose.lower() == "evacuation":
        return {
            "required": "Expedited process",
            "emergency_procedure_available": True,
            "documentation_needed": [
                "Any available identification",
                "Evacuation order if available",
                "Emergency contact in destination country"
            ],
            "processing_time": "Immediate to 24 hours for evacuation cases",
            "contact": f"{destination.title()} Emergency Management Office: +1-555-EVAC-NOW"
        }
    else:
        return {
            "required": "Standard process applies",
            "emergency_procedure_available": False,
            "documentation_needed": [
                "Passport valid for 6 months",
                "Visa application",
                "Proof of accommodation and return travel",
                "Proof of funds"
            ],
            "processing_time": "5-10 business days",
            "contact": f"{destination.title()} Embassy: consular@{destination.lower()}.embassy.example.org"
        } 
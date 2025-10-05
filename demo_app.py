from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

class DemoRequirementProcessor:
    def generate_specification(self, requirement):
        # Simulate processing time
        time.sleep(2)
        
        return """
## Technical Specification for Sporty Partners

### 1. Overview
Sporty Partners is a mobile application platform designed to connect sports enthusiasts in Sweden for recreational activities and competitive tournaments.

### 2. Functional Requirements
- **User Registration & Authentication**
  - Age verification (18+ only)
  - Profile creation with sports preferences
  - Skill level assessment and tracking
  
- **Partner Matching System**
  - Location-based search (GPS integration)
  - Time-based availability matching
  - Skill level compatibility filtering
  - Multi-sport category support
  
- **Meeting Coordination**
  - In-app messaging system
  - Event scheduling and calendar integration
  - Meeting location suggestions
  
- **Tournament Management**
  - Tournament creation and administration
  - Team registration system
  - Bracket generation and management
  - Results tracking and leaderboards

### 3. Non-functional Requirements
- **Performance**: Support 10,000+ concurrent users
- **Security**: End-to-end encryption for messaging
- **Availability**: 99.9% uptime
- **Scalability**: Horizontal scaling capability
- **Localization**: Swedish language support

### 4. Technical Constraints
- iOS and Android mobile platforms
- GDPR compliance for EU users
- Real-time messaging capabilities
- Offline functionality for basic features

### 5. Dependencies
- GPS/Location services
- Push notification services
- Payment gateway (for premium features)
- Map integration (Google Maps/Apple Maps)
"""

    def generate_user_stories(self, requirement):
        time.sleep(2)
        
        return """
## User Stories for Sporty Partners

### Epic 1: User Onboarding
- **As a** sports enthusiast **I want** to create a profile with my sports preferences **so that** I can find compatible partners
- **Acceptance Criteria**: 
  - Age verification (18+)
  - Sports selection from comprehensive list
  - Skill level self-assessment
  - Profile photo upload

### Epic 2: Partner Discovery
- **As a** user **I want** to search for sports partners by location **so that** I can find nearby activities
- **Acceptance Criteria**:
  - GPS-based location search
  - Distance radius selection (1-50km)
  - Real-time availability display
  - Filter by sport type and skill level

- **As a** casual player **I want** to find relaxed games **so that** I can enjoy sports without pressure
- **Acceptance Criteria**:
  - Skill level filtering (beginner/intermediate/advanced)
  - Activity type tags (competitive/casual/social)
  - Time preference matching

### Epic 3: Meeting Coordination
- **As a** user **I want** to message potential partners **so that** I can coordinate meeting details
- **Acceptance Criteria**:
  - Secure in-app messaging
  - Meeting proposal system
  - Calendar integration
  - Location sharing capabilities

### Epic 4: Tournament Participation
- **As a** competitive player **I want** to join tournaments **so that** I can compete with teams
- **Acceptance Criteria**:
  - Tournament search and filtering
  - Team formation tools
  - Registration and payment processing
  - Bracket viewing and updates

### Epic 5: Safety & Security
- **As a** user **I want** safety verification features **so that** I feel secure meeting new people
- **Acceptance Criteria**:
  - User verification badges
  - Rating and review system
  - Report and block functionality
  - Emergency contact features
"""

    def validate_output(self, tech_spec, user_stories):
        time.sleep(1)
        
        return """
## AI Validation Report

### 1. Completeness Score: 8.5/10

### 2. Key Strengths Found:
✅ **Comprehensive Coverage**: All major features addressed
✅ **User-Centric Design**: Clear focus on user needs and safety
✅ **Technical Feasibility**: Realistic technical requirements
✅ **Scalability Considerations**: Performance and growth planning included
✅ **Compliance Awareness**: GDPR and age verification addressed

### 3. Areas for Improvement:
⚠️ **Payment Integration**: Premium features mentioned but not detailed
⚠️ **Content Moderation**: Need specific policies for user-generated content
⚠️ **Data Analytics**: Missing user behavior tracking requirements
⚠️ **API Integration**: Third-party service dependencies need more detail

### 4. Recommendations:
1. **Add detailed payment flow** for tournament fees and premium features
2. **Specify content moderation algorithms** and community guidelines
3. **Include analytics dashboard** requirements for administrators
4. **Define API rate limits** and third-party service SLAs
5. **Add accessibility requirements** for inclusive design

### 5. Risk Assessment:
- **Low Risk**: Core matching and messaging functionality
- **Medium Risk**: Tournament management complexity
- **High Risk**: Safety verification and user trust systems

**Overall Assessment**: Well-structured requirements with strong user focus. Ready for development with minor enhancements to technical specifications.
"""

processor = DemoRequirementProcessor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_requirement():
    data = request.json
    requirement = data.get('requirement', '')
    
    if not requirement:
        return jsonify({'error': 'No requirement provided'}), 400
    
    # Generate outputs using demo data
    tech_spec = processor.generate_specification(requirement)
    user_stories = processor.generate_user_stories(requirement)
    validation = processor.validate_output(tech_spec, user_stories)
    
    return jsonify({
        'technical_specification': tech_spec,
        'user_stories': user_stories,
        'validation': validation
    })

if __name__ == '__main__':
    app.run(debug=True, port=5002)

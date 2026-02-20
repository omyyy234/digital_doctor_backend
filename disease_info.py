"""
🌿 Disease Knowledge Base
Contains treatment advice, descriptions, and 7-day action plans
for all 38 PlantVillage dataset classes + extensible for custom classes.
"""

# ── PlantVillage 38 Class Labels (standard order) ────────────
PLANTVILLAGE_LABELS = [
    "Apple___Apple_scab",
    "Apple___Black_rot",
    "Apple___Cedar_apple_rust",
    "Apple___healthy",
    "Blueberry___healthy",
    "Cherry_(including_sour)___Powdery_mildew",
    "Cherry_(including_sour)___healthy",
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot",
    "Corn_(maize)___Common_rust_",
    "Corn_(maize)___Northern_Leaf_Blight",
    "Corn_(maize)___healthy",
    "Grape___Black_rot",
    "Grape___Esca_(Black_Measles)",
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)",
    "Grape___healthy",
    "Orange___Haunglongbing_(Citrus_greening)",
    "Peach___Bacterial_spot",
    "Peach___healthy",
    "Pepper,_bell___Bacterial_spot",
    "Pepper,_bell___healthy",
    "Potato___Early_blight",
    "Potato___Late_blight",
    "Potato___healthy",
    "Raspberry___healthy",
    "Soybean___healthy",
    "Squash___Powdery_mildew",
    "Strawberry___Leaf_scorch",
    "Strawberry___healthy",
    "Tomato___Bacterial_spot",
    "Tomato___Early_blight",
    "Tomato___Late_blight",
    "Tomato___Leaf_Mold",
    "Tomato___Septoria_leaf_spot",
    "Tomato___Spider_mites Two-spotted_spider_mite",
    "Tomato___Target_Spot",
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
    "Tomato___Tomato_mosaic_virus",
    "Tomato___healthy",
]

def format_label(raw_label: str) -> str:
    """Convert 'Tomato___Early_blight' → 'Tomato Early Blight'"""
    parts = raw_label.replace("___", " — ").replace("_", " ")
    return parts.title()

# ── Disease Detail Database ───────────────────────────────────
# Each key matches a raw label. Add your own custom diseases below.
DISEASE_DATABASE = {

    # ── TOMATO ────────────────────────────────────────────────
    "Tomato___Early_blight": {
        "severity": "medium",
        "description": "Early blight is a common fungal disease causing dark brown spots with yellow rings on older leaves. It spreads quickly in warm, humid conditions and can significantly reduce yield.",
        "treatment": [
            "Remove and destroy infected leaves immediately",
            "Apply copper-based fungicide (e.g. Blitox 50) every 7-10 days",
            "Avoid overhead watering — water at the base only",
            "Ensure 60cm spacing between plants for airflow",
            "Apply neem oil spray as an organic alternative",
        ],
        "pesticide": "Mancozeb 75% WP @ 2.5g/litre OR Chlorothalonil 75% WP @ 2g/litre",
        "soil_treatment": "Add compost to improve drainage. Avoid waterlogging.",
    },
    "Tomato___Late_blight": {
        "severity": "high",
        "description": "Late blight is a highly destructive disease caused by Phytophthora infestans. It can destroy an entire crop within days if untreated. Dark water-soaked lesions appear on leaves and fruit.",
        "treatment": [
            "Remove and burn all infected plant material urgently",
            "Apply systemic fungicide (Metalaxyl + Mancozeb) immediately",
            "Spray every 5-7 days during humid weather",
            "Avoid working in the field when plants are wet",
            "Consider preventive spraying on healthy nearby plants",
        ],
        "pesticide": "Ridomil Gold (Metalaxyl 8% + Mancozeb 64%) @ 2.5g/litre",
        "soil_treatment": "Improve field drainage. Avoid planting in same location next season.",
    },
    "Tomato___Bacterial_spot": {
        "severity": "medium",
        "description": "Bacterial spot causes small dark water-soaked spots on leaves, stems, and fruit. It spreads through rain splash and infected seeds.",
        "treatment": [
            "Remove heavily infected leaves and fruit",
            "Apply copper hydroxide spray (Kocide) every 7 days",
            "Avoid working among wet plants to prevent spread",
            "Use disease-free certified seeds next season",
        ],
        "pesticide": "Copper Hydroxide 77% WP (Kocide) @ 3g/litre",
        "soil_treatment": "Rotate crops — do not plant tomatoes in same field for 2 years.",
    },
    "Tomato___Leaf_Mold": {
        "severity": "medium",
        "description": "Leaf mold thrives in high humidity greenhouses or dense plantings. Yellow patches appear on upper leaf surfaces with olive-green mold underneath.",
        "treatment": [
            "Improve ventilation around plants",
            "Reduce irrigation frequency",
            "Apply chlorothalonil or mancozeb fungicide",
            "Remove and destroy affected leaves",
        ],
        "pesticide": "Chlorothalonil 75% WP @ 2g/litre",
        "soil_treatment": "Ensure proper drainage and reduce soil moisture.",
    },
    "Tomato___Septoria_leaf_spot": {
        "severity": "medium",
        "description": "Septoria leaf spot causes circular spots with dark borders and light centers. It starts on lower leaves and moves upward, causing premature defoliation.",
        "treatment": [
            "Remove infected lower leaves promptly",
            "Apply mancozeb or copper fungicide spray",
            "Avoid wetting foliage when irrigating",
            "Mulch around base to prevent soil splash",
        ],
        "pesticide": "Mancozeb 75% WP @ 2.5g/litre",
        "soil_treatment": "Mulch the base. Improve drainage.",
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "severity": "medium",
        "description": "Spider mites are tiny pests that suck plant sap, causing yellow stippling and fine webbing on leaves. They thrive in hot, dry conditions.",
        "treatment": [
            "Spray plants with strong water jet to dislodge mites",
            "Apply neem oil or insecticidal soap spray",
            "Introduce predatory mites (biological control)",
            "Apply miticide if infestation is severe",
        ],
        "pesticide": "Abamectin 1.8% EC @ 0.5ml/litre OR Neem Oil @ 5ml/litre",
        "soil_treatment": "Keep soil moist — mites prefer dry conditions.",
    },
    "Tomato___Target_Spot": {
        "severity": "medium",
        "description": "Target spot causes circular lesions with concentric rings resembling a target. It affects leaves, stems, and fruit.",
        "treatment": [
            "Apply chlorothalonil or azoxystrobin fungicide",
            "Remove infected plant debris",
            "Improve plant spacing for air circulation",
        ],
        "pesticide": "Azoxystrobin 23% SC @ 1ml/litre",
        "soil_treatment": "Rotate crops and destroy plant debris after harvest.",
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "severity": "high",
        "description": "TYLCV is a virus spread by whiteflies. Infected plants show curled yellow leaves, stunted growth, and dramatically reduced fruit production. There is no cure — prevention and vector control are critical.",
        "treatment": [
            "Remove and destroy infected plants immediately to prevent spread",
            "Control whitefly population with yellow sticky traps",
            "Apply imidacloprid or thiamethoxam insecticide for whitefly control",
            "Use reflective mulch to deter whiteflies",
            "Plant resistant varieties in future seasons",
        ],
        "pesticide": "Imidacloprid 17.8% SL @ 0.3ml/litre for whitefly control",
        "soil_treatment": "No soil treatment. Focus on insect vector control.",
    },
    "Tomato___Tomato_mosaic_virus": {
        "severity": "high",
        "description": "Tomato mosaic virus causes mottled light and dark green patterns on leaves, leaf distortion, and reduced fruit quality. It spreads through contact and infected tools.",
        "treatment": [
            "Remove and destroy infected plants",
            "Disinfect all tools with bleach solution (10%) between uses",
            "Wash hands thoroughly before handling plants",
            "Control aphids which can spread the virus",
            "Use virus-free certified seeds",
        ],
        "pesticide": "No direct cure. Control aphid vectors with Thiamethoxam 25% WG @ 0.3g/litre",
        "soil_treatment": "Remove all infected plant debris. Do not compost infected material.",
    },
    "Tomato___healthy": {
        "severity": "none",
        "description": "Your tomato crop appears healthy! No disease detected. Continue your current care routine.",
        "treatment": [
            "Maintain regular watering schedule",
            "Apply balanced fertilizer every 2-3 weeks",
            "Monitor regularly for early signs of disease",
            "Keep field weed-free",
        ],
        "pesticide": "Preventive: Neem oil spray @ 5ml/litre every 2 weeks",
        "soil_treatment": "Regular compost application recommended.",
    },

    # ── POTATO ────────────────────────────────────────────────
    "Potato___Early_blight": {
        "severity": "medium",
        "description": "Potato early blight causes dark concentric ring spots on older leaves. It reduces photosynthesis and can lower tuber yield if severe.",
        "treatment": [
            "Remove infected leaves from the base upward",
            "Apply mancozeb or chlorothalonil fungicide",
            "Ensure proper plant spacing",
            "Avoid excessive nitrogen fertilization",
        ],
        "pesticide": "Mancozeb 75% WP @ 2.5g/litre, spray every 10 days",
        "soil_treatment": "Ensure well-drained soil. Add potassium-rich fertilizer.",
    },
    "Potato___Late_blight": {
        "severity": "high",
        "description": "Potato late blight (same pathogen as the Irish Famine) is extremely destructive. Water-soaked lesions turn brown and plants collapse rapidly. Tubers can also be infected.",
        "treatment": [
            "Act immediately — this disease can destroy a crop in 3-5 days",
            "Apply Metalaxyl + Mancozeb (Ridomil) urgently",
            "Remove and burn all infected haulm (plant tops)",
            "Do not harvest until 2 weeks after haulm destruction",
            "Check tubers for infection before storing",
        ],
        "pesticide": "Ridomil Gold @ 2.5g/litre. Repeat every 5-7 days.",
        "soil_treatment": "Deeply bury or burn crop debris. Do not replant potatoes for 3 years.",
    },
    "Potato___healthy": {
        "severity": "none",
        "description": "Your potato crop looks healthy! Continue monitoring and maintaining good practices.",
        "treatment": [
            "Hill up soil around stems to protect tubers",
            "Maintain consistent soil moisture",
            "Apply balanced NPK fertilizer",
            "Scout for Colorado potato beetle weekly",
        ],
        "pesticide": "Preventive copper spray every 2-3 weeks in humid weather",
        "soil_treatment": "Add compost before planting for best results.",
    },

    # ── CORN / MAIZE ──────────────────────────────────────────
    "Corn_(maize)___Common_rust_": {
        "severity": "medium",
        "description": "Common rust produces powdery orange-brown pustules on both leaf surfaces. It spreads rapidly in cool, moist conditions.",
        "treatment": [
            "Apply triazole fungicide (propiconazole or tebuconazole) at first sign",
            "Spray in early morning for best absorption",
            "Plant rust-resistant hybrid varieties next season",
            "Avoid dense planting",
        ],
        "pesticide": "Propiconazole 25% EC @ 1ml/litre",
        "soil_treatment": "Balanced potassium nutrition reduces rust severity.",
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "severity": "medium",
        "description": "Northern leaf blight causes long gray-green cigar-shaped lesions on corn leaves, reducing photosynthesis and yield.",
        "treatment": [
            "Apply fungicide at tasseling stage if lesions appear on upper leaves",
            "Use resistant hybrid varieties",
            "Remove crop debris after harvest",
            "Rotate with non-host crops",
        ],
        "pesticide": "Azoxystrobin + Propiconazole (Quilt Xcel) @ 1.5ml/litre",
        "soil_treatment": "Incorporate crop residue into soil after harvest.",
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "severity": "medium",
        "description": "Gray leaf spot causes rectangular gray to tan lesions between leaf veins. It is favored by warm, humid conditions and reduced tillage systems.",
        "treatment": [
            "Apply strobilurin or triazole fungicide",
            "Improve field drainage",
            "Plant resistant varieties",
            "Rotate with soybean or other non-host crops",
        ],
        "pesticide": "Trifloxystrobin + Propiconazole @ 1.5ml/litre",
        "soil_treatment": "Tillage helps reduce surface residue where spores overwinter.",
    },
    "Corn_(maize)___healthy": {
        "severity": "none",
        "description": "Your maize crop looks healthy! Keep up the good work.",
        "treatment": [
            "Apply top-dress nitrogen at knee-high stage",
            "Monitor for fall armyworm regularly",
            "Maintain adequate soil moisture",
        ],
        "pesticide": "Preventive: Scout and use pheromone traps for armyworm",
        "soil_treatment": "Apply urea top-dressing after first weeding.",
    },

    # ── APPLE ─────────────────────────────────────────────────
    "Apple___Apple_scab": {
        "severity": "medium",
        "description": "Apple scab causes dark, scabby lesions on leaves and fruit, making apples unmarketable and reducing tree vigor.",
        "treatment": [
            "Apply myclobutanil or captan fungicide during wet spring weather",
            "Rake and destroy fallen leaves",
            "Prune trees for better air circulation",
            "Apply lime sulfur spray during dormant season",
        ],
        "pesticide": "Myclobutanil 10% WP @ 1g/litre OR Captan 50% WP @ 2.5g/litre",
        "soil_treatment": "Remove and compost fallen leaves away from orchard.",
    },
    "Apple___Black_rot": {
        "severity": "high",
        "description": "Black rot causes brown leaf spots, mummified fruit, and cankers on branches. Infected fruit turns completely black.",
        "treatment": [
            "Prune out all dead or cankered wood",
            "Remove mummified fruit from trees and ground",
            "Apply captan or thiophanate-methyl fungicide",
            "Paint pruning wounds with copper paste",
        ],
        "pesticide": "Captan 50% WP @ 2.5g/litre, spray every 10-14 days",
        "soil_treatment": "Bury or burn fallen infected fruit and leaves.",
    },
    "Apple___Cedar_apple_rust": {
        "severity": "medium",
        "description": "Cedar apple rust causes bright orange-yellow spots on apple leaves and fruit, requiring both apple and cedar/juniper trees to complete its life cycle.",
        "treatment": [
            "Apply myclobutanil fungicide at pink bud stage",
            "Remove nearby cedar/juniper trees if possible",
            "Plant rust-resistant apple varieties",
            "Continue fungicide program through petal fall",
        ],
        "pesticide": "Myclobutanil 10% WP @ 1g/litre",
        "soil_treatment": "No special soil treatment required.",
    },
    "Apple___healthy": {
        "severity": "none",
        "description": "Your apple tree looks healthy! Maintain your spray program and monitoring.",
        "treatment": [
            "Continue regular dormant oil spray program",
            "Monitor for codling moth with pheromone traps",
            "Apply balanced fertilizer in spring",
        ],
        "pesticide": "Preventive dormant oil spray before bud break",
        "soil_treatment": "Apply compost mulch around base, away from trunk.",
    },

    # ── GRAPE ─────────────────────────────────────────────────
    "Grape___Black_rot": {
        "severity": "high",
        "description": "Grape black rot causes brown leaf spots and turns berries into hard black mummies. It can destroy the entire crop if not managed early.",
        "treatment": [
            "Remove mummified berries and infected leaves",
            "Apply mancozeb or myclobutanil at bud break",
            "Continue sprays every 10-14 days through veraison",
            "Improve canopy management for airflow",
        ],
        "pesticide": "Myclobutanil 10% WP @ 1g/litre or Mancozeb @ 2.5g/litre",
        "soil_treatment": "Remove all plant debris from vineyard floor.",
    },
    "Grape___Esca_(Black_Measles)": {
        "severity": "high",
        "description": "Esca is a complex grapevine trunk disease causing tiger-stripe leaf patterns and sudden vine collapse. It is caused by several wood-rotting fungi.",
        "treatment": [
            "No effective chemical cure — management is preventive",
            "Prune during dry weather to avoid infection",
            "Apply wound sealant paste after pruning",
            "Remove and destroy severely infected vines",
            "Delay pruning until late in the dormant season",
        ],
        "pesticide": "Thiophanate-methyl as wound protectant after pruning",
        "soil_treatment": "Improve drainage. Avoid water stress which worsens symptoms.",
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "severity": "medium",
        "description": "Leaf blight causes dark angular spots on grape leaves leading to premature defoliation and weakened vines.",
        "treatment": [
            "Apply copper-based fungicide at first sign",
            "Remove infected leaves promptly",
            "Improve vine training for better air circulation",
        ],
        "pesticide": "Copper oxychloride 50% WP @ 3g/litre",
        "soil_treatment": "Mulch to reduce soil splash onto lower leaves.",
    },
    "Grape___healthy": {
        "severity": "none",
        "description": "Your grapevine looks healthy! Continue your spray calendar.",
        "treatment": [
            "Follow preventive fungicide calendar",
            "Train and trim shoots for good airflow",
            "Monitor for downy and powdery mildew",
        ],
        "pesticide": "Preventive copper + sulfur program during growing season",
        "soil_treatment": "Apply potassium-rich fertilizer to improve fruit quality.",
    },

    # ── OTHER CROPS ───────────────────────────────────────────
    "Orange___Haunglongbing_(Citrus_greening)": {
        "severity": "high",
        "description": "Citrus greening (HLB) is the most destructive citrus disease worldwide. It is caused by bacteria spread by the Asian citrus psyllid. There is currently no cure.",
        "treatment": [
            "Remove and destroy infected trees immediately to prevent spread",
            "Control Asian citrus psyllid with systemic insecticides",
            "Apply nutritional sprays to slow decline in mildly affected trees",
            "Plant certified disease-free nursery stock only",
            "Report to local agricultural authority — this is a notifiable disease",
        ],
        "pesticide": "Imidacloprid soil drench for psyllid control",
        "soil_treatment": "Foliar micronutrient spray (zinc + manganese + boron) to support tree.",
    },
    "Peach___Bacterial_spot": {
        "severity": "medium",
        "description": "Bacterial spot causes water-soaked lesions on peach leaves and fruit, leading to defoliation and unmarketable fruit.",
        "treatment": [
            "Apply copper hydroxide at shuck split stage",
            "Repeat every 7-10 days during wet weather",
            "Avoid overhead irrigation",
            "Plant resistant varieties",
        ],
        "pesticide": "Copper hydroxide 77% WP @ 2g/litre",
        "soil_treatment": "Improve drainage. Avoid excess nitrogen which increases susceptibility.",
    },
    "Pepper,_bell___Bacterial_spot": {
        "severity": "medium",
        "description": "Bacterial spot on pepper causes dark raised spots on leaves and fruit, leading to defoliation and yield loss.",
        "treatment": [
            "Apply copper-based bactericide spray",
            "Use disease-free seeds and transplants",
            "Avoid working with wet plants",
            "Rotate with non-solanaceous crops",
        ],
        "pesticide": "Copper oxychloride 50% WP @ 3g/litre",
        "soil_treatment": "Rotate crops for minimum 2 years.",
    },
    "Squash___Powdery_mildew": {
        "severity": "medium",
        "description": "Powdery mildew appears as white powdery coating on leaves, reducing photosynthesis and fruit quality.",
        "treatment": [
            "Apply potassium bicarbonate or sulfur-based fungicide",
            "Spray neem oil as organic option",
            "Improve air circulation around plants",
            "Avoid excessive nitrogen fertilization",
        ],
        "pesticide": "Sulfur 80% WDG @ 2.5g/litre OR Tebuconazole @ 1ml/litre",
        "soil_treatment": "Avoid waterlogging which increases humidity.",
    },
    "Strawberry___Leaf_scorch": {
        "severity": "medium",
        "description": "Leaf scorch causes purple-red blotches on strawberry leaves that enlarge and coalesce, causing leaf edges to look scorched.",
        "treatment": [
            "Remove old infected foliage after harvest",
            "Apply myclobutanil or captan fungicide",
            "Avoid overhead irrigation",
            "Renovate beds to improve air circulation",
        ],
        "pesticide": "Captan 50% WP @ 2.5g/litre",
        "soil_treatment": "Renovate beds and apply fresh mulch after harvest.",
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "severity": "medium",
        "description": "Powdery mildew on cherry causes white powdery growth on young leaves and shoots, curling leaves and reducing fruit size.",
        "treatment": [
            "Apply sulfur or triazole fungicide at first sign",
            "Prune to improve canopy airflow",
            "Avoid excess nitrogen fertilization",
        ],
        "pesticide": "Myclobutanil 10% WP @ 1g/litre",
        "soil_treatment": "Balanced fertilization — avoid excess nitrogen.",
    },
}

# ── Healthy classes shortcut ──────────────────────────────────
HEALTHY_LABELS = {l for l in PLANTVILLAGE_LABELS if "healthy" in l.lower()}

# ── Fallback for unknown diseases ────────────────────────────
DEFAULT_DISEASE_INFO = {
    "severity": "unknown",
    "description": "A disease has been detected in your crop. Please consult your local agricultural extension officer for specific treatment advice.",
    "treatment": [
        "Isolate affected plants to prevent spread",
        "Remove and destroy visibly infected leaves",
        "Consult local agricultural officer for diagnosis confirmation",
        "Apply broad-spectrum copper fungicide as precautionary measure",
    ],
    "pesticide": "Copper oxychloride 50% WP @ 3g/litre as general treatment",
    "soil_treatment": "Improve drainage and avoid waterlogging.",
}

def get_disease_info(raw_label: str) -> dict:
    """Get full disease info dict for a given label."""
    return DISEASE_DATABASE.get(raw_label, DEFAULT_DISEASE_INFO)

def get_action_plan(raw_label: str) -> list:
    """Generate a 7-day action plan based on disease severity."""
    info = get_disease_info(raw_label)
    severity = info.get("severity", "medium")
    is_healthy = raw_label in HEALTHY_LABELS

    if is_healthy:
        return [
            {"day": 1, "task": "Inspect full field", "details": "Walk the entire field and note any early warning signs."},
            {"day": 2, "task": "Check soil moisture", "details": "Ensure irrigation system is working properly."},
            {"day": 3, "task": "Apply preventive spray", "details": "Neem oil @ 5ml/litre as a preventive measure."},
            {"day": 4, "task": "Weed management", "details": "Remove weeds that compete with crops and harbour pests."},
            {"day": 5, "task": "Fertilizer check", "details": "Assess crop nutrition and apply if needed."},
            {"day": 6, "task": "Pest scouting", "details": "Check undersides of leaves for pests or eggs."},
            {"day": 7, "task": "Document crop status", "details": "Photograph and record crop condition for future reference."},
        ]

    if severity == "high":
        return [
            {"day": 1, "task": "🚨 URGENT: Isolate & remove", "details": "Mark infected area. Remove all visibly infected plant material and burn or bury far from field."},
            {"day": 2, "task": "First fungicide application", "details": f"Apply {info.get('pesticide', 'recommended fungicide')} immediately. Cover all leaf surfaces."},
            {"day": 3, "task": "Check spread to neighbors", "details": "Inspect plants surrounding the infected area. Mark any new infections."},
            {"day": 4, "task": "Second spray if wet weather", "details": "Re-apply fungicide if rain occurred. Check for new lesions on previously healthy plants."},
            {"day": 5, "task": "Soil treatment", "details": info.get("soil_treatment", "Check drainage and remove infected debris.")},
            {"day": 6, "task": "Assess recovery", "details": "Check treated plants for signs of recovery. Document any spread."},
            {"day": 7, "task": "Final assessment + report", "details": "Evaluate success of treatment. If no improvement, contact agricultural extension officer urgently."},
        ]
    else:
        return [
            {"day": 1, "task": "Remove infected material", "details": "Remove infected leaves and plant parts. Do not leave them in the field."},
            {"day": 2, "task": "First fungicide/treatment spray", "details": f"Apply {info.get('pesticide', 'recommended treatment')} in early morning."},
            {"day": 3, "task": "Improve growing conditions", "details": info.get("soil_treatment", "Check soil drainage and plant spacing.")},
            {"day": 4, "task": "Monitor for spread", "details": "Inspect treated plants and adjacent rows. Remove any new infected material."},
            {"day": 5, "task": "Second treatment application", "details": "Apply second round of treatment, especially if humid conditions persist."},
            {"day": 6, "task": "Nutrition support", "details": "Apply foliar micronutrient spray to boost plant immune response."},
            {"day": 7, "task": "Review & document", "details": "Compare to Day 1. Take photos. If condition has worsened, consult agricultural officer."},
        ]


# ── CUSTOM 6-CLASS MODEL DISEASES ────────────────────────────
# These match the likely classes of your AutoML Vision model
CUSTOM_6_CLASS_DATABASE = {
    "Healthy": {
        "severity": "none",
        "description": "Your crop appears completely healthy! No disease detected. Continue your current care routine and monitor regularly.",
        "treatment": [
            "Maintain regular watering schedule",
            "Apply balanced NPK fertilizer every 2-3 weeks",
            "Monitor weekly for early signs of disease",
            "Keep field weed-free to reduce pest harborage",
        ],
        "pesticide": "Preventive: Neem oil spray @ 5ml/litre every 2 weeks",
        "soil_treatment": "Apply compost to maintain soil health.",
    },
    "Powdery_Mildew": {
        "severity": "medium",
        "description": "Powdery mildew appears as white powdery coating on leaf surfaces. It spreads rapidly in warm days and cool nights with high humidity, reducing photosynthesis and yield.",
        "treatment": [
            "Remove and destroy heavily infected leaves immediately",
            "Apply sulfur-based fungicide or potassium bicarbonate spray",
            "Spray neem oil (5ml/litre) as an organic alternative",
            "Improve air circulation by spacing plants properly",
            "Avoid overhead irrigation — water at the base",
            "Avoid excess nitrogen fertilization which promotes soft growth",
        ],
        "pesticide": "Sulfur 80% WDG @ 2.5g/litre OR Tebuconazole 25% EC @ 1ml/litre",
        "soil_treatment": "Avoid waterlogging. Ensure good drainage to reduce humidity.",
    },
    "Rust": {
        "severity": "medium",
        "description": "Rust disease produces orange-brown powdery pustules on leaves and stems. It spreads rapidly through wind-dispersed spores in cool, moist conditions and can cause significant yield loss.",
        "treatment": [
            "Remove and burn infected plant material",
            "Apply triazole fungicide (propiconazole or tebuconazole) at first sign",
            "Spray in early morning for best absorption",
            "Repeat spray every 10-14 days during humid weather",
            "Plant rust-resistant varieties in future seasons",
        ],
        "pesticide": "Propiconazole 25% EC @ 1ml/litre OR Mancozeb 75% WP @ 2.5g/litre",
        "soil_treatment": "Balanced potassium nutrition reduces rust severity. Avoid excess nitrogen.",
    },
    "Leaf_Blight": {
        "severity": "medium",
        "description": "Leaf blight causes large irregular brown to tan lesions on leaves that expand rapidly, leading to premature defoliation and weakened plants. It is caused by fungal or bacterial pathogens.",
        "treatment": [
            "Remove infected leaves from the base upward",
            "Apply copper-based fungicide spray immediately",
            "Ensure proper plant spacing for airflow",
            "Avoid overhead irrigation",
            "Mulch around base to prevent soil splash",
            "Rotate crops next season",
        ],
        "pesticide": "Copper oxychloride 50% WP @ 3g/litre OR Chlorothalonil 75% WP @ 2g/litre",
        "soil_treatment": "Improve drainage. Remove all infected debris after harvest.",
    },
    "Early_Blight": {
        "severity": "medium",
        "description": "Early blight is a common fungal disease causing dark brown spots with concentric rings (like a target) on older leaves first. It spreads upward in warm, humid conditions and can significantly reduce yield.",
        "treatment": [
            "Remove and destroy infected leaves immediately",
            "Apply copper-based fungicide (Blitox/Mancozeb) every 7-10 days",
            "Avoid overhead watering — water at the base only",
            "Ensure adequate spacing between plants for airflow",
            "Apply neem oil spray as an organic alternative",
            "Stake plants to keep foliage off the ground",
        ],
        "pesticide": "Mancozeb 75% WP @ 2.5g/litre OR Chlorothalonil 75% WP @ 2g/litre",
        "soil_treatment": "Add compost to improve drainage. Mulch to prevent soil splash onto leaves.",
    },
    "Late_Blight": {
        "severity": "high",
        "description": "Late blight is one of the most destructive crop diseases. Water-soaked lesions appear on leaves and rapidly turn dark brown. It can destroy an entire crop within 3-5 days under humid, cool conditions. Act immediately.",
        "treatment": [
            "🚨 ACT IMMEDIATELY — this disease spreads extremely fast",
            "Remove and BURN all infected plant material urgently",
            "Apply systemic fungicide (Metalaxyl + Mancozeb) right away",
            "Spray every 5-7 days during humid or rainy weather",
            "Avoid working in the field when plants are wet",
            "Apply preventive spray to all healthy nearby plants",
            "Improve field drainage urgently",
        ],
        "pesticide": "Ridomil Gold (Metalaxyl 8% + Mancozeb 64%) @ 2.5g/litre — spray IMMEDIATELY",
        "soil_treatment": "Improve field drainage. Do not plant same crop in same location next season.",
    },
}

# Merge into main database so get_disease_info() works for all classes
DISEASE_DATABASE.update(CUSTOM_6_CLASS_DATABASE)
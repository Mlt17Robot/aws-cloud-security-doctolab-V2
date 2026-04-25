import json
import boto3

sns = boto3.client('sns')

TOPIC_ARN = "arn:aws:sns:eu-west-3:187528943763:macie-alerts"

def lambda_handler(event, context):
    detail = event.get("detail", {})
    
    bucket = detail.get("resourcesAffected", {}).get("s3Bucket", 
{}).get("name", "Unknown")
    objects = detail.get("resourcesAffected", {}).get("s3Object", {})
    
    file_name = objects.get("key", "Unknown")
    
    severity = detail.get("severity", {}).get("description", "Unknown")
    title = detail.get("title", "Macie Alert")

    message = f"""
🚨 ALERTE SÉCURITÉ - AWS MACIE

📦 Bucket : {bucket}
📄 Fichier : {file_name}
⚠️ Type : {title}
🔥 Sévérité : {severity}

👉 Action recommandée :
- Vérifier le contenu du fichier
- Supprimer ou sécuriser immédiatement
"""

    sns.publish(
        TopicArn=TOPIC_ARN,
        Subject="🚨 Alerte Sécurité Macie",
        Message=message
    )

    return {"status": "ok"}

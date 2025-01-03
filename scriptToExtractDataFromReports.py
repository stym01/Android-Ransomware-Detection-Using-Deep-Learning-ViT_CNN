import os
import json
import pandas as pd

def extract_features(json_data):
    """Extract features from the JSON data."""
    report_summary = {
        "filetype": None,
        "no_of_VirusTotal_positives": None,
        "total_no_of_permissions": 0,
        "dangerous_permissions": 0,
        "triggered_signatures": 0,
        "signature_severity": 0,
        "udp_count": 0,
        "File_identified_by_10_AVs": 0,
        "Hidden_Payload_Found": 0,
        "Application_Asks_For_Dangerous_Permissions": 0,
        "no_of_Hosts_Involved": 0,
        "label": None,  # Add label column
    }

    # Extract filetype if present
    report_summary["filetype"] = json_data.get("target", {}).get("file", {}).get("type", None)

    # Extract VirusTotal positives
    virustotal_data = json_data.get("virustotal", {})
    report_summary["no_of_VirusTotal_positives"] = virustotal_data.get("positives", 0)

    # Analyze permissions
    permissions = json_data.get("apkinfo", {}).get("manifest", {}).get("permissions", [])
    report_summary["total_no_of_permissions"] = len(permissions)
    for permission in permissions:
        if permission.get("severity", "").lower() == "dangerous":
            report_summary["dangerous_permissions"] += 1

    # Extract triggered signatures and their severities
    signatures = json_data.get("signatures", [])
    report_summary["triggered_signatures"] = len(signatures)

    # Extract UDP count
    network_data = json_data.get("network", {})
    udp_data = network_data.get("udp", [])
    report_summary["udp_count"] = len(udp_data)

    # Check for specific indicators in signatures
    for signature in signatures:
        if "File has been identified by more the 10 AntiVirus on VirusTotal as malicious" in signature.get("description", ""):
            report_summary["File_identified_by_10_AVs"] = 1
        if "Hidden Payload Found" in signature.get("description", ""):
            report_summary["Hidden_Payload_Found"] = 1
        if "Application Asks For Dangerous Permissions" in signature.get("description", ""):
            report_summary["Application_Asks_For_Dangerous_Permissions"] = 1

    # Extract the number of hosts involved
    hosts = network_data.get("hosts", [])
    report_summary["no_of_Hosts_Involved"] = len(hosts)

    return report_summary

def process_dataset(dataset_path, label):
    """Process all report.json files in the dataset and extract features."""
    data = []
    for folder_name in os.listdir(dataset_path):
        folder_path = os.path.join(dataset_path, folder_name)
        if os.path.isdir(folder_path):
            reports_folder = os.path.join(folder_path, "reports")
            report_file = os.path.join(reports_folder, "report.json")
            if os.path.exists(report_file):
                try:
                    with open(report_file, "r") as file:
                        json_data = json.load(file)
                    features = extract_features(json_data)
                    features["label"] = label  # Set label based on dataset
                    data.append(features)
                except Exception as e:
                    print(f"Error processing {report_file}: {e}")
    return pd.DataFrame(data)

# Define dataset paths and output file
benign_path = r"D:\Data Ransomware\analysis\benign"
malicious_path = r"D:\Data Ransomware\analysis\malicious"
output_csv_path = "features_extracted4.csv"

# Process both benign and malicious datasets
benign_df = process_dataset(benign_path, label=0)  # Label 0 for benign
malicious_df = process_dataset(malicious_path, label=1)  # Label 1 for malicious

# Combine the data and save to CSV
dataset = pd.concat([benign_df, malicious_df])
dataset.to_csv(output_csv_path, index=False)
print(f"Features saved to {output_csv_path}")

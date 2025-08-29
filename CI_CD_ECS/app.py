from flask import Flask, render_template, jsonify

app = Flask(__name__)

portfolioData = {
  "name": "Pranesh Kumar C",
  "title": "AWS Data Engineer",
  "contact": {
    "email": "praneshc2004btc@gmail.com",
    "phone": "+91 6369995300",
    "linkedin": "https://www.linkedin.com/in/pranesh-kumar-c-58298924a",
    "github": "https://github.com/praneshkumarc",
  },
  "summary": "A results-driven AWS Certified Data Engineer with a passion for building scalable data pipelines and robust cloud infrastructure. Proficient in Java and Python, with hands-on experience in designing and deploying highly available, automated solutions on AWS. Adept at leveraging soft skills like agile development and team collaboration to deliver high-quality projects.",
  "education": {
    "degree": "Bachelor of Technology in Computer Science",
    "university": "Amrita Vishwa Vidyapeetham, Coimbatore",
    "years": "2022 – 2026",
    "cgpa": "6.19 / 10.0"
  },
  "skills": {
    "Programming": ["Java", "Python", "SQL", "Shell Scripting"],
    "Cloud & Data Engineering": ["AWS (S3, EC2, Redshift, Glue, Lambda, RDS, Athena, Kinesis)", "ETL/ELT", "Data Warehousing", "Data Modeling", "Data Lake Architecture"],
    "Web Development": ["React.js", "Node.js", "Express.js", "Tailwind CSS", "Redux", "RESTful APIs"],
    "DevOps & CI/CD": ["Docker", "Kubernetes (EKS)", "AWS CodePipeline", "Jenkins", "GitHub Actions", "Git"],
    "Databases": ["MongoDB", "Mongoose", "Amazon RDS"],
    "Monitoring & Security": ["CloudWatch", "IAM", "VPC"],
    "Soft Skills": ["Agile Development", "Problem Solving", "Team Collaboration", "Communication"]
  },
  "certifications": [
    { "name": "AWS Certified Cloud Practitioner", "issuer": "Amazon Web Services", "id": "cloud-practitioner" },
    { "name": "Generative AI Engineering with LLMs", "issuer": "Coursera (Educator: IBM)", "id": "gen-ai-eng" },
    { "name": "AWS Cloud Solutions Architect", "issuer": "Coursera (Educator: AWS)", "id": "coursera-sa" },
    { "name": "AWS Academy Data Engineering Badge", "issuer": "AWS Academy", "id": "aws-academy-data-badge" }
  ],
  "projects": [
    {
      "title": "Full CI/CD Pipeline with AWS Developer Tools",
      "category": "Cloud Engineering",
      "description": "Implemented a complete, automated CI/CD pipeline on AWS...",
      "elaboration": [
        "**Source Control:** Utilized AWS CodeCommit ...",
        "**Build & Test:** Configured AWS CodeBuild ...",
        "**Deployment:** Leveraged AWS CodeDeploy ...",
        "**Orchestration:** Integrated all services using AWS CodePipeline ..."
      ],
      "tags": ["AWS CodePipeline", "CodeCommit", "CodeBuild", "CodeDeploy", "EC2", "IAM"]
    },
    {
      "title": "Highly Available & Auto-Scaling Web Application",
      "category": "Cloud Architecture",
      "description": "Designed and deployed a fault-tolerant, highly available web application on AWS...",
      "elaboration": [
        "**Load Balancing:** ALB distributes traffic ...",
        "**Auto Scaling:** ASG scales instances ...",
        "**Database:** Amazon RDS Multi-AZ ...",
        "**Stateless Application:** Sessions offloaded ..."
      ],
      "tags": ["EC2", "Auto Scaling", "ELB", "RDS Multi-AZ", "VPC", "CloudWatch"]
    },
    {
      "title": "Containerized App with Blue/Green Deployment on ECS",
      "category": "DevOps & Containers",
      "description": "Built a containerized application using Docker and deployed it on Amazon ECS with automated blue/green ...",
      "elaboration": [
        "**Containerization:** Lightweight Docker image ...",
        "**Orchestration:** Amazon ECS manages tasks ...",
        "**Blue/Green with CodeDeploy:** New green task set ...",
        "**Traffic Shifting:** ALB listener rules shift traffic ..."
      ],
      "tags": ["ECS", "Docker", "AWS CodeDeploy", "Fargate", "ALB", "CI/CD"]
    },
    {
      "title": "EC2 in Private Subnet with Secure Internet Access",
      "category": "Cloud Security",
      "description": "Established a secure network architecture where an EC2 instance in a private subnet can access the internet ...",
      "elaboration": [
        "**VPC Setup:** Public & private subnets ...",
        "**Bastion Host:** OpenVPN ...",
        "**Private Instance:** No direct IGW route ...",
        "**Outbound Access:** NAT Gateway ..."
      ],
      "tags": ["VPC", "Subnets", "NAT Gateway", "OpenVPN", "Security Groups", "EC2"]
    },
    {
      "title": "Crypto Price Tracking App",
      "category": "Web Development",
      "description": "Real-time crypto market data with CoinGecko API ...",
      "tags": ["React.js", "CoinGecko API", "Tailwind CSS", "WebSockets"],
      "link": "#"
    },
    {
      "title": "Responsive Portfolio with Advanced Animations",
      "category": "Web Development",
      "description": "Personal portfolio using React.js and Tailwind CSS ...",
      "tags": ["React.js", "Tailwind CSS", "Responsive Design"],
      "link": "#"
    }
  ]
}

@app.route("/")
def home():
    return render_template("index.html", data=portfolioData)

@app.route("/healthz")
def healthz():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    # For local dev only; prod uses gunicorn
    app.run(host="0.0.0.0", port=8000)

import docker
import os
import sys 
import json
import requests
import mysql.connector
import urllib3 
import pymongo
from pymongo import MongoClient
import datetime
import uuid 
import socket

##Suppress the warning
urllib3.disable warnings (urllib3.exceptions. InsecureRequestWarning)


##Connection to MySQL Database
cnx = mysql.connector.connect (user='<user>', password=****, host='vm1', database='<db-name>')
cursor = cnx.cursor()
readcursor cnx.cursor (buffered=True)
readremote_dockerinfo = cnx.cursor (buffered=True)
readvicrates = cnx.cursor (buffered=True)
read autoscale_history = cnx.cursor (buffered=True)
read scaledown_containerid = cnx.cursor (buffered=True)


##Connection to MongoDB
mongo_client = MongoClient()
mongo_client = MongoClient (mongodb://<IPAddress>:<port>/')
db = mongo_client.test.database



##Read the Alerts for Autoscaling
autoscale records = db ["autoscale_request"]



#Get current date
month=datetime.datetime.now().month
year=datetime.datetime.now().year
day=datetime.datetime.now().year
vic_naming_convention = "No"



#Search for un processed recorda

#search_query("Id":"$regex": container_id), "year":year, "month":month) search query("Alert Status":"unprocessed")
search_query = {"Alert_Status":"unprocessed"}
autoscale_request = autoscale_records.find(search_query)



for x in autoscale_request:

    autoscale_action=x['autoscale action']

    if autoscale_action "service availability":
        request_id = x['_id"] 
        remote_docker_Name_full = x['metricset']['host']
        event = x['event']['dataset']
        container status = x['docker']['event']['status']
        container_image = x['docker']['event']['from'] container_name = x['docker']['event']['actor']['attributes']['name']
        #container_trefik_status=x['docker'1 ['event']['actor']['attributes']['traefik enable'l
        container_service_availability = x['docker']['event']['actor']['attributes']['service availability']
        container_id=x['docker']['event']['actor']['id']
        policy_name = x['vic_policy_name']

    if autoscale_action "scale_up":
        query=x['id']
        request_id = {"_id" :query)     
        container_id = x['docker']['container']['id']
        remote_docker_Name full = x['metricset']['host']
        total_cpu usage = x['metric_docker']['cpu']['total']['pct_avg']
        #autoscale_service_name = x['autoscale_service_name']
        autoscale_max_instances_str = x['autoscale_max_instances']
        autoscale_max_instances = int(autoscale_max_instances_str) 
        policy_name = x['vic policy_name']

        container_image = x['docker.container.image']

    if autoscale_action="scale_down":
        query = x[' id']
        request_id=("id":query)
        container_id=x['docker']['container']['id'] 
        remote_docker_Name_full = x['metricset']['host']
        total_cpu_usage = x['metric_docker']['cpu']['total']['pct avg']
        autoscale_service_name=x['autoscale_service_name']
        autoscale_min_instances_str = x['autoscale_min_instances']
        autoscale_min_instances = int(autoscale_min_instances_str) 
        policy_name = x['vic policy_name']

    if autoscale_action="scale_up_node":
        alert_service_name = x['alert_service_name']
        remote_docker_Name_full = x['metricset']['host'] 
        autoscale_max_instances_str = x['autoscale_max instances']
        autoscale_max_instances_int = int(autoscale_max_instances_str) 
        #autoscale_min_instances str = x['autoscale min instances'1
        autoscale_min_instances_int = (autoscale_min instances_str)

        policy_name=x['vic_policy_name']
        query=x['id']
        request_id = {"_id" :query)

    if autoscale_action="scale_down_node": 
        alert_service_name = x['alert_service_name']
        remote_docker Name full x['metricaet']['host']
        autoscale_max_instances_str = x['autoscale_max_instances'] 
        autoscale_max_instances = int(autoscale_max_instances str)
        policy_name = x['vic_policy_name']
        query = x['id'] 
        request_id = {"_id": query}
        autoscale_min_instances str = ['autoscale min instances']
        autoscale_min_instances = int(autoscale_min_instances_str)

    if autoscale_action "scale_up_service":
        alert_service_name = x['alert service name']
        remote_docker_Name_full = x['metricnet']['host']
        autoscale_max_instances_str = x['autoscale_max_instances']
        autoscale_max_instances = int(autoscale_max_instances_str)
        policy_name=x['vic_policy_name']
        query x['_id']
        request id= {"_id" :query}
        vic_naming_convention = x['vic naming convention']

    if autoscale_action="scale_down_service":
        alert_service_name=x['alert_service_name'] 
        remote_docker_Name_full = x['metricset']['host']
        policy_name = x['vic_policy_name']
        query=x['_id']
        request_id=("_id":query)
        autoscale_min_instances_str = x['autoscale_min_instances']
        autoscale_min_instances = int(autoscale_min_instances_str)

    if autoscale_action "haproxy_scale_up": 
        alert_service_name = x['alert_service_name']
        remote_docker_Name_full = x['metricset']['host'] 
        autoscale_max_instances_str=x['autoscale_max_instances'] 
        autoscale_max_instances = int(autoscale_max_instances_str) 
        policy name=x['vic_policy_name']
        query = x['_id']
        request_id = {"_id" :query)


    #Container frontend rule
    #Container backend rule
    remote_docker_Name_array = remote_docker_Name_full.split("")
    remote_docker_Name = remote_docker_Name_array[0]
    
    
    #Get the remote_docker details
    get_remote_docker_list = select remote_docker_Name, remote_docker Network, remote_docker Port, LOB, AppCode, PCCode, CVM Storage from vic_remote_docker_info where remote_docker_Name = remote_docker
    readremote_dockerinfo.execute (get_remote_docker list, (remote_docker Name,))
    remote_dockerinfo=readremote_dockerinfo.fetchone ()


    remote_docker_Name=remote_dockerinfo[0]
    remote_docker Network = remote_dockerinfo[1]
    remote_docker_Port = remote_dockerinfo[2]
    remote_docker_LOB=remote_dockerinfo[3]
    remote_docker_AppCode = vehinfo[4]
    remote_docker_PCCoderemote_dockerinfo[5]
    cvm_storage_confremote_dockerinfo[6]
    remote_docker_short_name = remote_docker_Name.split("")
    remote_docker Name = remote_docker_short_name[0]

    docker_host = str(remote_docker_Name) +str("<DOCKER_API>:<docker tls port>")
    docker_cert_path_str = str("/") +remote_docker Name remote_docker_cert_file-str("/") +remote_docker_Name+str("/")+"cert.pem"    
    remote_docker_key_file = str("/")+remote_docker_Name+str("/")+"key.pem"
    remote_docker_ca_file = str("/")+remote_docker_Name+str("/")+"ca.pem" 
    remote_docker_base_url = str("https://")+remote_docker Name+str("DOCKER_API:<docker tls port>")
    
    os.environ["DOCKER API VERSION")="1.25"
    os.environ("DOCKER TLS VERIFY"1="1"
    os.environ["COMPOSE TLS VERSION"]="TLSV1_2"
    os.environ["DOCKER_HOST"]=docker_host_str
    os.environ["DOCKER CERT PATH"]=docker_cert_path



    #print (Docker API)

    ##TLS Configuration for accensing remote_docker using Certificate

    tls_config = docker.cls.TLSConfig(client_cert-(remote_docker_cert file, remote_docker key file), ca_cert=remote_docker_ca_file,ssl_version='TLSv1_2')

    #client
    docker_cli = docker.DockerClient (base_url=remote_docker_base_url, tls=tls_config)
    
    #API
    docker_api=docker.APIClient(base_url=remote_docker_base_url, tis=tis_config, version="1.23")

    ##Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commande

    if autoscale_action = "scale_up_node" and autoscale_action = "scale_down_node" and autoscale_action="scale_up_service" and autoscale_action = "scale_down_service" and autoscale_action = "service_availability" and autoscale_action = "haproxy_scale_up": 
        container_inspect = docker_api.inspect_container(container_id)
        #cpu- container inspect'HostConfig']['CpusetCpus']
        #memory container_inspect['HostConfig']['Memory']
        #volume name container inspect['Mounts'1 [0] ['Name']

        container_image = container_inspect['Config']['Image'] 
        docker_labels = container_inspect['Config']['Labels']
        docker_network  = container_inspect['HostConfig']['NetworkMode']
        autoscale_service_name = docker_labels['vic service_name']

    ## Read Docker Labels
    # autoacale.min instances-docker labels("min instances"]
    # autoscate.max_instances docker_labels("max_instances"
    #Action copy it from Alert Notification
    # autoscale.action-docker labels ["action"]
    # autoscale.application name-docker labels["application_name"] 
    # autoscale.step-docker labels("step"]    
    #autoscale.min_cpu-docker_labels ["min_cpu"] 
    # autoscale.max_cpurdocker_labels ["max cpu")

    #autoscale.policy-stocker labela("policy"]
    
    ### Get the Autoscale policy based on docker label or Service Name. Docker Label will take the priority and then db configuration

    ##============Policy Type: Service Availability=================

    ##As part of Service Availability # If Service Stop, start the Service
    ##If Service Delete event, create new service from same image and pass docker labels from previous
    # Also chcek for how to silence the ElastAlert
    # Start the Container if stopped and service availability
    
    ##Add AND Condition for Event as Stop
    if autoscale_action = service availability":"
        docker_api.start (container id)
        search_autoscale_request - "id": ["$regex":request id))
        updated_autoscale_status =("set":{"Alert Status":"processed")) 
        db.autoscale_request = update_one(search_autoscale_request, updated autoscale status)

    #if autoacale action="service availability" AND event "die" 
    # create the container from sane image

    ##===================Policy Type: Scale Up==========
    #Take the min, max dynamically. Based on if condition of stats.
    # Check for Min Max value for number of container created against db as checking for container with same docker label in different remote_docker will be more cycle
    #Or Check for Min Max value captured through ElastAlert portal. And check for

    # Create the Containers
    #container

    client.containers.run(vic_image, cpuset_cpus = CPU, mem_limit = MEMORY, labels = docker_labels, network = remote_docker_Network, detach = True, volume[vol_sdk_param])

    if autoscale action = "scale_up": 
        #no_of_instances running = 0
        #filter_label = "vic_service_name=" + "
        #container_list_array = docker_api.containers(filter={"label":(filter_label)})
        #num_cVM_running = len(container_list_array)
        
        while num_CVM_running < autoscale_max_instances: 
            #Check Autoscale History for Hax & Min conatiners created for same policy
            #get_autoscale_policy="select COUNT (new containerid) from vic_autoscale history where policy rule applied and container statuss
            #read autoscale_history.execute(get_autoscale_policy, (autoscale service name, "running",))
            #autoscale_history-read autoscale history.fetchone ()

            filter_label="vic_service_name" + autoscale_service_name
            container_list_array = docker api.containers (filters={"label": (filter label) }) 
            num_cVM running = len(container_list_array)

            if num_cVM_running < autoscale_max_instances:
                container = docker.cli.containers.run(container_image,network=docker_network,labels=docker_labels,detach=True)
                container.reload()
                ip=container.attrs("NetworkSettings"] ["Networks"] [docker network] ["IPAddress"] ## Insert the record in Autoscale History
                add request("INSERT INTO vic_autoscale_history " "(remote_docker_name,containerod,policy_rule_applied,cpu_spike,container_status,service_name)"
                "VALUE (%s,%s,%s,%s,%s,%s)")
                add data = (remote_docker Name, container.id, policy_name, str (total_cpu usage). "running", autoscale_service_name]
                cursor execute (add request, add data)
                cnx.commit()

                search_autoscale request = request id 
                updated_autoscale_status="set": {"Alert Status":"processed"}}
                db.autoscale_request.update_one(search_autoacale_request, updated_autoscale_status)
            else:
                search_autoscale_request = request_id
                updated autoacale status = ("set":"Alert Status":"skipped"} 
                db.autoscale = request.update_one (search_autoscale_request, updated autoscale

        ###===============Policy Type: Scale Down=============

        ##Take the win, max dynamically. Based on if condiditon of stats
        ##Do the docker inspect using API to search for other scaled container based on label search, get container id and delete

        if autoscale_action = scale_down":
            #filter label-vic service name + autoscale service name
            #container list array docker apt. containera (filters-("label": (filter_label))) 
            #num CVM running len (container list array)
            #num CVM running = 200

            while num_cVM_running > autoacale_min_instances:
                #get_autoacale_policy"select COUNT (new_containerid) from vic autoscale history where policy rule applied is and container status "
                #read autoscale_history.execute (get_autoscale policy, (autoscale_service_name, "running",))
                #autoscale history-read autoscale_history.fetchone () 
                #no_of_instances running autoscale history [0]

                filter_label="vic_service_name-" + autoscale_service_name
                container_list_array = docker_api.containers (filters ("label": (filter label)), all=True)
                num_CVM_running = len(container_list_array)
                scaledown_containerid = container_list_array[0]['Id']

                #get_scaledown_containerid="select new_containerid from vic_autoscale_history where policy rule applied ts and container_statuss" 
                #read scaledown containerid.execute iger scaledown_containerid, (autoscale service name, "running",))


                if num_cVM running < autoscale_min_instances:
                    docker_api.remove_container(containerid, force=True)
                    # Update the record in Autoscale History for Scale Down Tracking 
                    update_requeat=("UPDATE vic_autoscale_history SET container_status=True, cpu_spikes WHERE containerids and service_name = %s ")
                    update_data("deleted",str(total cpu usage), str(scaledown_containerid), autoscale_service_name)
                    cursor.execute(update_request, update_data)
                    cnx.commit()

                    search autoacale_request = request id 
                    updated autoscale_statua("update":("Alert Status":"processed"))
                    db.autoscale = request.update_one(search_autoscale_request, updated_autoscale_status)

                else:
                    search autoacale request request id
                    updated = autoacale_status-("update": ("Alert Status":"akipped"))
                    db.autoscale = request.update_one(search autoscale request, updated_autoscale_status)

#=========================================================
# Policy Type: Dynamic Load Balancer (HAProxy, Nginx or Traefik). Once application is scale upscale down, check how to connect to load balancer. 
# Container should take care of connection LB dynamically based on label or API

#=============================================
# Policy Type: Monitor the Load Balancer (HAProxy, Nginx, Traefik, Envoy) Response Time. 
# Call above scale up & scale down application based on application alert. Above function can be reused

#=======================================================
# Logic: Capture the Service Name from Alert. Search for Container list using filter Label-service that Docker Label And apply the Scale Up & Scale Down policy

# Update the Database for Audit purpose.

#=====================================Traefik: Load Balancer Scale Up

    if autoscale_action = "scale_up_node" or autoscale_action "scale_up_service":
        filter_label="vic_service_name" + alert_service_name 
        container_list_array = docker_api.containers(filters("label": (filter_label} })
        #Count No of recorda
        num_CVM = len(container_list_array)

        ##Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commands 
        container_id = container_list_array[0]['Id']
        container_inspect = docker_api.inspect_container(container_id) 
        container_image = container_inspect['Config']['Image']
        docker_labels = container_inspect['Config']['Labels'] I

        #Based on number of container with that service name scale up and scale down 
        
        while num_VM < autoscale_max_instances:
            container_array = docker_api.containers(filters="label": (filter label)))
            num_CVM = len(container_list_array)
            if num_cVM < autoscale_max_instances: 
                if vic_naming_convention = "No":
                    auto numatr(uuid.uuids())
                    auto_num= auto num. replace ("-","")
                    auto_num= auto_num(0:12)
                    CVM_Name = vic_naming_convention + auto_num
                    container = docker_cli.containers.run (container image, network-remote_docker Network,labels=docker_labels, name=cVM_Name, tty=True, detac=True)
                    container.reload()
                else:
                    container = docker.cli.containers.run (container_image, network-remote_docker Network, labels-docker labels, tty-True, detach=True) 
                    container.reload()
                    ip = container.attrs["NetworkSettings"]["Networks"]["remote_docker_Network"]["IPAddress"]          
                # Insert the record in Autoscale History

                add_request ("INSERT INTO vic_autoscale_history" (remote_docker name, containerid, policy rule_applied,container_status,service_name)" 
                "VALUES (%s,%s,%s,%s)")

                add_data(remote_docker_Name, container.id,policy_name, "running", alert_service_name)
                cursor.execute(add_request, add data)
                cnx.commit()

                search_autoscale_request = request_id
                updated_autoscale_status-("set": ("Alert Status":"processed")) db.autoscale_request.update one (search_autoscale_request, updated autoscale_status)

            else:
                search_autoscale_request(request_id) 
                updated_autoscale_status = ("set":("Alert Status":"akipped"))
                db.autoscale_request.update_one(search_autoscale_request, updated_autoscale_status)


#============================Traefik: Load balancer Scale Down================

    if autoscate action = "scale_down_node" or autoscale_action = "scale_down_service":
        filter_label = vic_service_name+ alert service name
        container_list_array = docker_api.containers (Filters("label": (filter_label)) #Count No of records

        num CVM = len (container_list_array)
        num CVM = 10000
        
        while num_cVM> autoscale min instances: 
         container_list array docker_api.containera (filters("label":(filter_label))
         num_CVM = len(container_list_array)
         scaledown_containerid = container_list_array [0]['Id']

        if num CVM > autoscale min instances:
            docker api remove container (scaledown containerid, v=False, force=True)
            update_request={"UPDATE vic_autoscale history SET container_statuss WHERE containerid=5 and policy rule_applied = is ") cursor.execute (update_request, update_data)
            update data = ("deleted", str (scaledown_containerid),policy_name)
            cnx.commit()
            
            search autoscale_request request id
            updated autoscale_status={"aet":{"Alert_Status":"processed")) db.autoscale_request.update one (search_autoscale_request, updated_autoscale_status)
        else:
            search autoscale request = request_id
            updated_autoscale status="set": ["Alert Status":"skipped"}}
            db.autoscale_request.update one (search_autoscale_request, updated_autoscale_status)


##================HAProxy Load balancer Scale Up===========

    if autoscale action = "haproxy_scale_up":
        filter_label="vic_service_name" + alert_service_name I
        container_list_array = docker_api.containers(filters=["label": (filter_label)))

        #Count No of records
        num_cVM = len(container_list_array)

        #Inspect the container to get the Docker Label, cpu, memory, volume details required for docker run commands
        container_id container list array[0]['Id']
        container_inspect docker api.inspect container (container container image container inspect ['Config']['Image']
        docker_labels = container_inspect['Config']['Labels']
        
        #Get HAProxy label passed to Container
        haproxy_host = docker_labels['haproxy_host']
        haproxy_port = docker_labels['haproxy_port']
        haproxy_port = int (haproxy_port)
        vic_haproxy_backend = docker_labels['vic_haproxy_backend' ]
        vic_haproxy_node = docker_labels('vic_haproxy_node"] 
        vic_haproxy_backend app_port = docker_labels['vic_haproxy_backend_app_port'l

        vic_haproxy_backend_app_port-int (vic_haproxy_backend_app_port)

        num_cvm = 0

        #based on number of container with that service name scale up and scale down

        while num CVM < autoscale_max instances: 
            filter label-vic service name="+ alert service name
            container_list array = docker api.containers (filters-("label": (filter_label) })
            num CVM running len (container list_array) 
            haproxy_node_count = num CVM running+1
            
            if num cVM running < autoscale max_instances:
                container docker cli.containers.run(container_image, network-remote_docker Network, labels=docker_labels, detach-True)
                container.reload() 
                ip = container.attra("NetworkSettings" ["Networks"][remote_docker Network) ["IPAddress"]

                #Update the HAProxy Configuration Dynamically 
                haproxy_sock socket.socket (socket. AF INET, socket.SOCK_STREAM)
                haproxy nock.connect((haproxy hoat, haproxy port))
                command = "set server vic haproxy backend+/+vic_haproxy_node+haproxy_node_count addr ip port vic_haproxy backend app portla
                encode command command, encode ()
                haproxy sock, send (encode command)
                retval = ""
                while True:
                    buf = haproxy sock.recv (16)
                    if buf:
                        retval += buf
                    else:
                        break
                    haproxy sock.close()
                    
                    print (retval)

                    haproxy_sock = socket.socket (socket.AF_INET, socket.SOCK STREAM)
                    haproxy_sock.connect((haproxy_host,haproxy_port))
                    command="set server vic haproxy backend+/+vic_haproxy_node+haproxy_node_count state ready\n"
                    encode_command = command.encode()
                    haproxy sock.send (encode command)
                    retval = ""

                    while True:
                        buf = haproxy_sock.recv (16)
                        if buf:
                            retval += buf
                        else:
                            break
                    haproxy sock.close()
                    
                    print (retval)

                    ## Insert the record in Autoscale History:
                    
                    add_request-("INSERT INTO vic_autoscale_history" (remote_docker_name, containerid, policy rule_applied, container_status, service_name)" VALUES (%s,%s,%s,%s)")
                    add data = (remote_docker Hame, container.id, policy name, "running", alert_service_name)
                    cursor.execute (add request, add data)
                    cnx.commit()

                    search_autoscale_request = request_id
                    updated_autoscale_status = ("$set": {"Alert_Status":"processed"))
                    db.autoscale_request.update_one (search autoscale request, updated autoscale status)
            else:
                search_autoscale_request = request_id
                updated_autoscale_status = ("$set": ("Alert Status":"skipped")) 
                db.autoscale_request.update_one (search_autoscale request, updated autoscale status)


#Capture the Load Balancer Count, Response Time, No of record process and update

cursor.close()
cnx.close()
readremote_dockerinfo.close()

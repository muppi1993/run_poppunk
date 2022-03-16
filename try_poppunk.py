from PopPUNK.assign import assign_query
from PopPUNK.utils import setupDBFuncs
from PopPUNK.web import summarise_clusters
from PopPUNK.visualise import generate_visualisations
from types import SimpleNamespace
import json
import os

# loading sketch
file = '7553_4#5_sketch.json'
with open(file, 'r') as f:
    sketch = json.load(f)
sketch_json = json.dumps(sketch)

#defining species
species = 'Streptococcus pneumoniae'

# loading args
with open("args.json") as a:
    args_json = a.read()
args = json.loads(args_json, object_hook=lambda d: SimpleNamespace(**d))

# set database path
db_path = '/home/mmg220/Documents/poppunk'
db_name = 'GPS_v4'
species_db = db_path + '/' + db_name

# set output directory
outdir = "./WebOutput" 
if not os.path.exists(outdir):
    os.makedirs(outdir)

# create qc_dict
qc_dict = {'run_qc': False}

# create  dbFuncs
dbFuncs = setupDBFuncs(args=args.assign, qc_dict=qc_dict,
                       min_count=args.assign.min_kmer_count)

# run query assignment
assign_query(
    dbFuncs=dbFuncs,
    ref_db=species_db,
    q_files=outdir + '/queries.txt',
    output=outdir,
    qc_dict=qc_dict,
    update_db=args.assign.update_db,
    write_references=args.assign.write_references,
    distances=species_db + '/' + db_name + '.dists.pkl',
    threads=args.assign.threads,
    overwrite=args.assign.overwrite,
    plot_fit=args.assign.plot_fit,
    graph_weights=args.assign.graph_weights,
    max_a_dist=args.assign.max_a_dist,
    max_pi_dist=args.assign.max_pi_dist,
    type_isolate=args.assign.type_isolate,
    model_dir=species_db,
    strand_preserved=args.assign.strand_preserved,
    previous_clustering=species_db,
    external_clustering=args.assign.external_clustering,
    core_only=args.assign.core_only,
    accessory_only=args.assign.accessory_only,
    gpu_sketch=args.assign.gpu_sketch,
    gpu_dist=args.assign.gpu_dist,
    gpu_graph=args.assign.gpu_graph,
    deviceid=args.assign.deviceid,
    web=args.assign.web,
    json_sketch=sketch_json,
    save_partial_query_graph=args.assign.save_partial_query_graph
)

query, query_prevalence, clusters, prevalences, alias_dict, to_include = \
            summarise_clusters(outdir, species, species_db)

print("clusterID: " + query)


generate_visualisations(
    query_db=outdir,
    ref_db=species_db,
    distances=outdir + '/WebOutput.dists',
    #rank_fit=None,
    threads=args.visualise.threads,
    output=outdir,
    gpu_dist=args.visualise.gpu_dist,
    deviceid=args.visualise.deviceid,
    external_clustering=args.visualise.external_clustering,
    microreact=args.visualise.microreact,
    phandango=args.visualise.phandango,
    grapetree=args.visualise.grapetree,
    cytoscape=args.visualise.cytoscape,
    perplexity=args.visualise.perplexity,
    strand_preserved=args.visualise.strand_preserved,
    include_files= outdir + "/include.txt",
    model_dir=species_db,
    previous_clustering=species_db + '/' + db_name + '_clusters.csv',
    previous_query_clustering=args.visualise.previous_query_clustering,
    #previous_mst=None,
    #previous_distances=None,
    network_file=outdir + "/WebOutput_graph.gt",
    gpu_graph=args.visualise.gpu_graph,
    info_csv=args.visualise.info_csv,
    rapidnj=args.visualise.rapidnj,
    tree=args.visualise.tree,
    mst_distances=args.visualise.mst_distances,
    overwrite=args.visualise.overwrite,
    core_only=args.visualise.core_only,
    accessory_only=args.visualise.accessory_only,
    display_cluster=args.visualise.display_cluster,
    web=True
)

"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""
import os
from flask import Flask, render_template, make_response,redirect, url_for, send_from_directory
from flask import request, Response, send_file, redirect
from flask.views import View
app = Flask(__name__, template_folder='templates')
app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = set(['fasta'])
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in app.config['ALLOWED_EXTENSIONS']
@app.route('/')
def feat():
    return render_template("feat.html")

@app.route('/musclealign')
def musclealign():
    return render_template("muscle.html")

@app.route('/genese')
def genes():
    return render_template("genesearch.html")


@app.route('/phylotree')
def phylotree():
    return render_template("upload.html")

@app.route('/plotting')
def plotting():
    return render_template("plot upload.html")

@app.route('/blast')
def blast():
    return render_template("blast.html")

@app.route("/gotoindex")
def gotoindex():
    return render_template("index.html")

@app.route("/blastp")
def blastp():
    return render_template("blastp.html")

@app.route("/userguide")
def userguide():
    return render_template("userguide.html")

@app.route("/getPlotCSV")
def getPlotCSV():
    try:
        return send_file('Seq1.xml',
                         mimetype='text/xml',
                         download_name='BlastXML.xml',
                         as_attachment=True)
    except Exception as e:
        return f"An error occurred: {e}"


@app.route("/alignment",methods=['GET','POST'])
def alignment():
    return render_template("htmlout.html")

@app.route('/blas',methods=['GET','POST'])
def blas():
    try:
        if request.method == 'POST':
            res = request.form['fooput']
            import os
            with open('Seq.fasta', "w") as myfile:
                myfile.write(res)
            from Bio import SeqIO
            with open("Seq1.fasta", 'w') as file:
                for record in SeqIO.parse("Seq.fasta", "fasta"):
                    print(f"> {record.id}", file=file)
                    print(record.seq, file=file)
            ress = request.form['SELECT_DB']
            maxtar = request.form['maxTarget']
            evalu = request.form['eVal']
            rewar = request.form['MScores']
            wordsize = request.form['wordSize']
            tex = request.form['texthidden']
            from Bio.Blast.Applications import NcbiblastnCommandline, NcbiblastpCommandline
            from Bio.Seq import Seq
            from Bio.SeqRecord import SeqRecord
            from Bio import SeqIO, SearchIO
            import re
            with open(r"templates\features.html", "w") as outfile, open(r"uploads\Alignment.txt", "w") as outfile1:
                print("""{% extends "header.html" %}
        {% block head %}
        <title>Blast information</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
        <link rel="profile" href="http://www.w3.org/1999/xhtml/vocab" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="Generator" content="Drupal 7 (http://drupal.org)" />
        <link type="text/css" rel="stylesheet" href="//cdn.jsdelivr.net/bootstrap/3.3.7/css/bootstrap.css" media="all" />
        <script src="https://www.citrusgenomedb.org/sites/all/libraries/jstree/jstree.js?owlcpl"></script>
            <script src="https://code.jquery.com/jquery-1.12.4.min.js?owlcpl"></script>
            <script type="text/javascript">
            // JQuery controlling display of the alignment information (hidden by default)
            $(document).ready(function () {

                // Hide the alignment rows in the table
                // (ie: all rows not labelled with the class "result-summary" which contains the tabular
                // summary of the hit)
                $("#blast_report tr:not(.result-summary)").hide();
                $("#blast_report tr:first-child").show();

                // When a results summary row is clicked then show the next row in the table
                // which should be corresponding the alignment information
                $("#blast_report tr.result-summary").click(function () {
                    $(this).next("tr").toggle();
                    $(this).find(".arrow").toggleClass("up");
                });
            });
            </script>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
        <style>table, th, td {border:none ;border-collapse: collapse;}
        th, td {padding: 5px;text-align: left;}</style>
        {% endblock %}{% block content %}
        <div class="container" style="margin-top:12%; width:1100px">
        <form method="post" enctype="multipart/form-data">
        <fieldset class="collapsible panel panel-default form-wrapper" id="edit-b">
        <legend class="panel-heading"><a href="#" class="panel-title fieldset-legend" data-toggle="collapse" data-target="#edit-b > .collapse">Show Results</a></legend>
        <div class="panel-collapse collapse fade in"><div class="panel-body">
        <fieldset class="collapsible panel panel-default form-wrapper" id="edit-query">
        <legend class="panel-heading"><a href="#" class="panel-title fieldset-legend" data-toggle="collapse" data-target="#edit-query > .collapse">Blast Results</a></legend>
        <center><h1 class="panel-body">Blast Results</h1><h3 class="panel-body" style="text-align:justify; font-size:16px; font-weight:lighter;">BLAST finds regions of similarity between biological sequences. The program compares nucleotide or protein sequences to sequence databases and calculates the statistical significance. </h3>""", file=outfile)  # Continue with the rest of your template string
                # Further processing and file operations
            if tex == "nucleotide":
                periden = request.form['periden']
                rewar = re.split(r",", rewar)
                gappen = request.form['gapCost1']
                gappen = re.split(r",", gappen)
                try:
                    blastn_cline = NcbiblastnCommandline(cmd='blastn', query="Seq1.fasta", db=ress, word_size=wordsize, gapopen=int(gappen[0]), gapextend=int(gappen[1]), reward=int(rewar[0]), penalty=int(rewar[1]), perc_identity=periden, max_target_seqs=maxtar, evalue=evalu, outfmt=11, out="Seq.xml")
                    stdout, stderr = blastn_cline()
                except:
                    os.system(str(blastn_cline))
                #blastn_cline = NcbiblastnCommandline(query="Seq1.fasta", db="PAKISTANLANGRA", evalue=0.001, outfmt=11, out="Seq.xml", word_size=11, max_target_seqs=500, gapopen=5, gapextend=2, penalty=-2, reward=1, perc_identity=0)
                #stdout, stderr = blastn_cline()
                cline = blastn_cline
            elif tex == "protein":
                gappen = request.form['gapCost1']
                gappen = re.split(r",", gappen)
                try:
                    blastp_cline = NcbiblastpCommandline(cmd='blastp', query="Seq1.fasta", db=ress, word_size=wordsize, gapopen=int(gappen[0]), gapextend=int(gappen[1]), matrix=rewar, max_target_seqs=maxtar, evalue=evalu, outfmt=11, out="Seq.xml")
                    stdout, stderr = blastp_cline()
                except:
                    os.system(str(blastp_cline))
                cline = blastp_cline

            os.system("blast_formatter -archive Seq.xml -out Seq1.xml -outfmt 5")
            os.system("blast_formatter -archive Seq.xml -out templates\\htmlout.html -html")
            E_VALUE_THRESH = 0.01
            import re
            from Bio.Blast import NCBIXML
            with open("templates/features.html", "a") as outfile:
                # Process each record in the NCBIXML output
                for record in NCBIXML.parse(open("Seq1.xml")):
                    print(f"<h2 class='panel-body' style='text-align:left; font-size:20px; font-weight:bold; margin-top:-25px'>Download Files: <a href='/getPlotCSV' style='color:gray;font-size:16px; font-weight:lighter;'>Xml File</a><a href='/alignment' style='color:gray;font-size:16px; font-weight:lighter;'>, Alignment</a></h2>", file=outfile)
                    print(f"<p class='panel-body' style='margin-top:-25px; text-align:justify;'><b>Database Name: </b>{record.database}<br/><b>Database Sequences: </b>{record.database_sequences}<br/><b>Blast Application: </b>{record.application}<br/><b>Blast Version: </b>{record.version}<br/><b>Blastn Command Executed: </b>{cline}</p>", file=outfile)
                    break  # Break after the first record for demo purposes; remove if all records are needed

                # Use SearchIO to parse the blast results
                qresults = SearchIO.parse('Seq1.xml', 'blast-xml')
                with open('qresult.txt', 'w') as out:
                    for q in qresults:
                        print(f"{q}", file=out)
        
                with open('qresult.txt') as my:
                    data = my.read()
        
                print(f"<pre class='panel-body' style='text-align:left; background:inherit'>{data}</pre>", file=outfile)
                print("<h3 class='panel-body' style='text-align:justify; font-size:16px; font-weight:lighter;'>The table below summarizes the results of your BLAST. Please click on a target name or anywhere in a row to see the alignment.</h3><div class='panel-body'><div class='table-responsive'><table id='blast_report' class='table table-hover table-striped'>", file=outfile)
                print("<thead style='background-color:#b5b4b4'><tr><th class='number'>S.No</th><th>Hit</th><th>Hsp</th><th>QueryID</th><th class='query'>Target Name  (Click for alignment)</th><th>Length</th><th class='evalue'>E-Value</th><th>Score</th><th>Gaps</th> </tr></thead><tbody>", file=outfile)

                d = 1
                for record in NCBIXML.parse(open("Seq1.xml")):
                    if record.alignments:
                        for align in record.alignments:
                            counter = 1
                            for hsp in align.hsps:
                                if hsp.expect < E_VALUE_THRESH:
                                    print(f"<tr class='result-summary'><td class='number'>{d}</td><td>{d}</td><td>{counter}</td><td>{record.query_id}</td><td class='query'>{align.title}</td><td>{align.length}</td><td class='evalue'>{hsp.expect:.4g}</td><td>{hsp.score}</td><td>{hsp.gaps}</td></tr>", file=outfile)
                                    d += 1
                                    counter += 1

                print("</tbody></table></div><h2>No of Hits found: {}</h2><br/></center></fieldset></div></div>".format(d-1), file=outfile)
                q_dict= SeqIO.index("Seq1.fasta", "fasta")
                hits=[]
                for records in NCBIXML.parse(open("Seq1.xml")):
                    if records.alignments:
                        hits.append(records.query.split()[0])
                misses = set(q_dict.keys()) - set(hits) 
                orphan_records = [q_dict[name] for name in misses]
                if len(hits)==0:
                    print("""</div></div></div><h3 style="text-align:center">No Records Found <br/>found %i records in query, %i have hits, making %i misses</h3>""" % (len(q_dict), len(hits), len(misses)), file=outfile)
                else:
                    print("""</div></div></div><h3 style="text-align:center">found %i records in query, %i have hits, making %i misses</h3>""" % (len(q_dict), len(hits), len(misses)), file=outfile)
                    print("""</fieldset></form></div>{% endblock %}""", file=outfile)
            outfile.close()
            app.jinja_env.cache = {}
        return render_template("features.html")

            # Additional exception handling as required
    except Exception as e:
        return str(e)






if __name__ == '__main__':
    
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)

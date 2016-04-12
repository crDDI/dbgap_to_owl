# dbgap_to_owl
Convert the [dbGaP XML Schema](ftp://ftp.ncbi.nlm.nih.gov/dbgap/xsl/dbGaPEx2.1.5.xsd) to an ISO 11179-3 compliant OWL representation

## Requirements
* python3 (ideally >= 3.5, but any 3.x version will do).  You can determine whether you have python on your machine and its version by:
  * `python -v` -- if 3.x you are ready to go, otherwise...
  * `python3 -v` -- if this works you are also ready to go
* virtualenv -- if this isn't on your machine, see <http://pythoncentral.io/how-to-install-virtualenv-python/>
* java -- we need version 1.7 or greater


## Installation
Set up a python3 virtual environment:

```bash
> virtualenv dbgaptoowl -p python3
> . dbgaptoowl/bin/activate
(dbgaptoowl) > pip install dbgap-to-owl
```

## Clone the modified PyXB executable
In an appropriate temporary directory:

``` bash
> (dbgaptoowl) > cd temp
> (dbgaptoowl) > git clone https://github.com/crDDI/pyxb.git
> (dbgaptoowl) > cd pyxb
> (dbgaptoowl) > python setup.py install
...
changing mode of [...]dbgaptoowl/bin/pyxbwsdl to 755
running install_egg_info
Writing [...]/dbgaptoowl/lib/python3.5/site-packages/PyXB-1.2.5_DEV-py3.5.egg-info
> (dbgaptoowl) > (cd back to working directory)
```

Note that the git clone step may take a while (we will see whether we can't merge this with the official PyXB branch at some point in the future)

## Run the conversion
Convert dbGaPEx2.1.5.xsd starting at the GaPExchange element, placing the output in dbGapEx2.1.5.ttl

```bash
(dbgaptoowl) > dbgaptoowl -i ftp://ftp.ncbi.nlm.nih.gov/dbgap/xsl/dbGaPEx2.1.5.xsd -o data/dbGapEx2.1.5.ttl -e GaPExchange
Attribute None.groupNum-REF renamed to groupNum_REF
Attribute DAC.dac-fax renamed to dac_fax
(dbgaptoowl) >
```




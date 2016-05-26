import os
import las_file_helper as lfh

class las_file:

    def __init__(self):

        self.curve_names = []
        self.curve_units = []
        self.curve_desciption = []
        self.curve_data = []

        self.start_depth = None
        self.stop_depth = None
        self.step_rate = None
        self.depth_units = ''
        self.null_value = None
        self.company_name = ''
        self.well_name = ''
        self.field = ''
        self.location = ''
        self.location2 = ''
        self.county = ''
        self.state = ''
        self.country = ''
        self.section = ''
        self.township = ''
        self.range = ''
        self.province = ''
        self.service_company = ''
        self.log_date = ''
        self.run_number = ''
        self.uwi = ''
        self.api = ''
        self.license = ''
        self.rig = ''
        self.permanent_datum = ''
        self.drill_meas_from = ''
        self.start_time = ''
        self.end_time = ''
        self.log_meas_from = ''
        self.latitude = ''
        self.longitude = ''
        self.projection = ''
        self.tvdss_correction = ''
        self.ground_elevation = ''
        self.utm_x = ''
        self.utm_y = ''
        self.utm_zone = ''
        self.per_datum_elevation = ''
        self.apd = ''
        self.magnetic_declination = ''
        self.kb_elevation = ''
        self.df_elevation = ''
        self.bit_size = ''
        self.geodetic_datum = ''

        ## Mud Data
        self.mud_type = ''
        self.mud_density = ''
        self.mud_viscosity = ''
        self.mud_ph = ''
        self.mud_fluid_loss_rate = ''
        self.mud_sample_source = ''
        self.mud_resistivity = ''
        self.mud_sample_temp = ''
        self.mud_filtrate_resistivity = ''
        self.mud_filtrate_sample_temp = ''
        self.mud_filtrate_sample_source = ''
        self.mud_cake_resistivity = ''
        self.mud_cake_sample_temp = ''
        self.mud_cake_sample_source = ''
        self.mud_logging_job_number = ''

        self.source_file = ''
        self.source_file_las_version = ''
        self.source_file_delimiter = ''
        self.errors = []
        #TODO keep track of all incoming parameters
        self.parameters = []
        self.other_infomation = []
        
        self.status = ''
        self.classification = ''
        self.formation_at_td = ''
        self.spud_date = ''
        self.completion_date = ''
        self.original_company = ''
        self.loggers_name = ''
        self.witness_name = ''
        self.logging_run_td = ''
        self._mud_resistivity_at_bht = ''
        self.max_temperature = ''   
        
    def write(self, file_path):
        entry_spacing = 40
        with open(file_path, 'w') as f:
            f.write('~Version Information Block \n')
            f.write('VERS .' + str(lfh.right_align_text('2.0', entry_spacing)) + ' : CWLS LOG ASCII STANDARD\n')
            f.write('WRAP .' + str(lfh.right_align_text('NO',entry_spacing)) + ' : Data Line Wrap\n')
            f.write('~Well Information Block\n')
            f.write('#MNEM.UNIT                                DATA : Data Description\n')
            f.write('#--------------------------------------------------------------------------------\n')
            f.write('STRT .' + lfh.entry(self.start_depth, self.depth_units, entry_spacing) + ' : Start Depth\n')
            f.write('STOP .' + lfh.entry(self.stop_depth, self.depth_units, entry_spacing) + ' : Stop Depth\n')
            f.write('STEP .' + lfh.entry(self.step_rate, self.depth_units, entry_spacing) + ' : Step Rate\n')
            f.write('NULL .' + lfh.entry(self.null_value, '', entry_spacing) + ' : Null Value\n')
            f.write('COMP .' + lfh.entry(self.company_name, '', entry_spacing) + ' : Company Name\n')
            f.write('WELL .' + lfh.entry(self.well_name, '', entry_spacing) + ' : Well Name\n')
            f.write('FLD  .' + lfh.entry(self.field, '', entry_spacing) + ' : Field\n')
            f.write('LOC  .' + lfh.entry(self.location, '', entry_spacing) + ' : Location\n')
            f.write('TOWN .' + lfh.entry(self.township, '', entry_spacing) + ' : Township\n')
            f.write('RANG .' + lfh.entry(self.range, '', entry_spacing) + ' : Range\n')
            f.write('SECT .' + lfh.entry(self.section, '', entry_spacing) + ' : Section\n')
            f.write('CNTY .' + lfh.entry(self.county, '', entry_spacing) + ' : County\n')
            f.write('STAT .' + lfh.entry(self.state, '', entry_spacing) + ' : State\n')
            f.write('CTRY .' + lfh.entry(self.country, '', entry_spacing) + ' : Country\n')
            f.write('SRVC .' + lfh.entry(self.service_company, '', entry_spacing) + ' : Service\n')
            f.write('DATE .' + lfh.entry(self.log_date, '', entry_spacing) + ' : Log Date\n')
            f.write('UWI  .' + lfh.entry(self.uwi, '', entry_spacing) + ' : Unique Well Identifier\n')
            f.write('API  .' + lfh.entry(self.api, '', entry_spacing) + ' : API Number\n')
            f.write('EPD  .' + lfh.entry(self.per_datum_elevation, self.depth_units, entry_spacing) + ' : Permanent Datum Elevation\n')
            f.write('LMF  .' + lfh.entry(self.log_meas_from, '', entry_spacing) + ' : Log Measured From\n')
            f.write('EGL  .' + lfh.entry(self.ground_elevation,self.depth_units, entry_spacing) + ' : Ground Level Elevation\n')
            f.write('BS   .' + lfh.entry(self.bit_size, 'in', entry_spacing) + ' : Bit Size\n')
            f.write('LATI .' + lfh.entry(self.latitude, '', entry_spacing) + ' : Latitude\n')
            f.write('LONG .' + lfh.entry(self.longitude, '', entry_spacing) + ' : Longitude\n')
            f.write('~Parameter Information Block\n')
            f.write('#MNEM.UNIT                                  DATA : Data Description\n')
            f.write('#--------------------------------------------------------------------------------\n')
            # TODO: add parameter section
            f.write('~Curve Information Block\n')
            f.write('#MNEM.UNIT                                   API : Curve Description\n')
            f.write('#--------------------------------------------------------------------------------\n')
            for i in range(len(self.curve_names)):
                f.write(lfh.curve_line(self.curve_names[i], self.curve_units[i], self.curve_desciption[i]) + '\n')
            f.write('#Curve Data \n')
            f.write('~A    ')
            for i in range(len(self.curve_names)):
                f.write(lfh.right_align_text(self.curve_names[i], 16))
            f.write('\n')
            for i in range(len(self.curve_data[0])):
                f.write('      ')
                for j in range(len(self.curve_names)):
                    f.write(lfh.right_align_text(self.curve_data[j][i],16))
                f.write('\n')
            
def read(file_path):
    if os.path.exists(file_path) == False:
        print('File path does not exist for LAS: ' + str(file_path))
        return -1
    l = las_file()
    l.source_file = file_path
    lines = []
    with open(file_path, 'r') as f:
        lines = f.read().split('\n')
    data_wrap = False
    delimiter = ' '
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip()
        if lines[i].startswith('~V'):
            i += 1
            while lines[i].startswith('~') == False:
                if lines[i].startswith('#') == False and len(lines[i]) > 0:
                    variable = str(lines[i])[0:lines[i].index('.')].strip()
                    value = str(lines[i])[lines[i].index('.')+1:lines[i].index(':')].strip()
                    #print str(variable) + '\t' + str(value)
                    if variable == 'VERS':
                        l.source_file_las_version = value
                    if variable == 'WRAP':
                        if value.upper().startswith('N'):
                            data_wrap = False
                        else:
                            data_wrap = True
                        #print('Data Wrap: ' + str(data_wrap))
                    # if variable == 'DLM':     ## TODO: NOT IMPLEMENTED
                i += 1
            i -= 1
        if lines[i].startswith('~W') or lines[i].startswith('~P'):
            #print 'Well info found'
            i += 1
            while lines[i].startswith('~') == False:
                if lines[i].startswith('#') == False and len(lines[i]) > 0:
                    variable = str(lines[i])[0:lines[i].index('.')].strip()
                    dot = lines[i].index('.')
                    space = lines[i][dot+1:].index(' ') + dot
                    colon = lines[i].index(':')
                    if variable == 'STRT':                        
                        l.depth_units = lines[i][dot+1:space+1].strip()
                        l.start_depth = lines[i][space+1:colon].strip()                        
                    if variable == 'STOP':                        
                        l.stop_depth = lines[i][space+1:colon].strip()
                    if variable == 'NULL':
                        l.null_value = lines[i][space+1:colon].strip()
                    if variable == 'STEP':
                        l.step_rate = lines[i][space+1:colon].strip()
                    if variable == 'COMP':
                        l.company_name = lines[i][space+1:colon].strip()
                    if variable == 'WELL':
                        l.well_name = lines[i][space+1:colon].strip()
                    if variable == 'LOC':
                        l.location = lines[i][space+1:colon].strip()
                    if variable == 'LOC2':
                        l.location2 = lines[i][space+1:colon].strip()
                    if variable == 'FLD':
                        l.field = lines[i][space+1:colon].strip()
                    if variable == 'CNTY':
                        l.county = lines[i][space+1:colon].strip()
                    if variable == 'PROV':
                        l.province = lines[i][space+1:colon].strip()
                    if variable == 'STAT':
                        l.state = lines[i][space+1:colon].strip()
                    if variable == 'CTRY':
                        l.country = lines[i][space+1:colon].strip()
                    if variable == 'SRVC':
                        l.service_company = lines[i][space+1:colon].strip()
                    if variable == 'DATE':
                        l.log_date = lines[i][space+1:colon].strip()
                    if variable == 'API':
                        l.api = lines[i][space+1:colon].strip()
                    if variable == 'UWI':
                        l.uwi = lines[i][space+1:colon].strip()
                    if variable == 'SECT':
                        l.section = lines[i][space+1:colon].strip()
                    if variable == 'TOWN':
                        l.township = lines[i][space+1:colon].strip()
                    if variable == 'RANG':
                        l.range = lines[i][space+1:colon].strip()
                    if variable == 'RUN':
                        l.run_number = lines[i][space+1:colon].strip()
                    if variable == 'LIC':
                        l.license = lines[i][space+1:colon].strip()
                    if variable == 'RIG':
                        l.rig = lines[i][space+1:colon].strip()
                    if variable == 'PDAT':
                        l.permanent_datum = lines[i][space+1:colon].strip()
                    if variable == 'DMF':
                        l.drill_meas_from = lines[i][space+1:colon].strip()
                    if variable == 'STIM':
                        l.start_time = lines[i][space+1:colon].strip()
                    if variable == 'LMF' or variable == 'DREF':
                        l.log_meas_from = lines[i][space+1:colon].strip()
                    if variable == 'LATI':
                        l.latitude = lines[i][space+1:colon].strip()
                    if variable == 'LONG':
                        l.longitude = lines[i][space+1:colon].strip()
                    if variable == 'TVDS':
                        l.tvdss_correction = lines[i][space+1:colon].strip()
                    if variable == 'EGL':
                        l.ground_elevation = lines[i][space+1:colon].strip()
                    if variable == 'UTMX':
                        l.utm_x = lines[i][space+1:colon].strip()
                    if variable == 'UTMY':
                        l.utm_y = lines[i][space+1:colon].strip()
                    if variable == 'EPD':
                        l.per_datum_elevation = lines[i][space+1:colon].strip()
                    if variable == 'APD':
                        l.apd = lines[i][space+1:colon].strip()
                    if variable == 'MDEC':
                        l.magnetic_declination = lines[i][space+1:colon].strip()
                    if variable == 'EKB':
                        l.kb_elevation = lines[i][space+1:colon].strip()
                    if variable == 'EDF':
                        l.df_elevation = lines[i][space+1:colon].strip()
                    if variable == 'BS':
                        l.bit_size = lines[i][space+1:colon].strip()
                    if  variable == 'GDAT':
                        l.geodetic_datum = lines[i][space+1:colon].strip()
                    if variable == 'MUD' or variable == 'DFT':
                        l.mud_type = lines[i][space+1:colon].strip()
                    if variable == 'MUDD':
                        l.mud_density = lines[i][space+1:colon].strip()
                    if variable == 'MUDV' or variable == 'DFV':
                        l.mud_viscosity = lines[i][space+1:colon].strip()
                    if variable == 'PH':
                        l.mud_ph = lines[i][space+1:colon].strip()
                    if variable == 'FL' or variable == 'DFL':
                        l.mud_fluid_loss_rate = lines[i][space+1:colon].strip()
                    if variable == 'MUDS' or variable == 'MSS':
                        l.mud_sample_source = lines[i][space+1:colon].strip()
                    if variable == 'RM':
                        l.mud_resistivity = lines[i][space+1:colon].strip()
                    if variable == 'RMT' or variable == 'MST':
                        l.mud_sample_temp = lines[i][space+1:colon].strip()
                    if variable == 'RMF':
                        l.mud_filtrate_resistivity = lines[i][space+1:colon].strip()
                    if variable == 'RMFS':
                        l.mud_filtrate_resistivity = lines[i][space+1:colon].strip()
                    if variable == 'RMFT':
                        l.mud_filtrate_sample_temp = lines[i][space+1:colon].strip()
                    if variable == 'MFSS':
                        l.mud_filtrate_sample_source = lines[i][space+1:colon].strip()
                    if variable == 'RMC' or variable == 'RMCS':
                        l.mud_cake_resistivity = lines[i][space+1:colon].strip()
                    if variable == 'RMCT' or variable == 'MCST':
                        l.mud_cake_sample_temp = lines[i][space+1:colon].strip()
                    if variable == 'MCSS':
                        l.mud_cake_sample_source = lines[i][space+1:colon].strip()
                i += 1
            i -= 1
        if lines[i].startswith('~C'):
            i += 1
            while lines[i].startswith('~') == False:
                if lines[i].startswith('#') == False and len(lines[i]) > 0:
                    variable = str(lines[i])[0:lines[i].index('.')].strip()
                    dot = lines[i].index('.')
                    space = lines[i][dot+1:].index(' ') + dot
                    colon = lines[i].index(':')                    
                    name = lines[i][0:dot].strip()
                    unit = lines[i][dot+1:colon].strip()
                    desc = lines[i][colon+1:].strip()
                    l.curve_names.append(name)
                    l.curve_units.append(unit)
                    l.curve_desciption.append(desc)
                i += 1
            i -= 1
        if lines[i].startswith('~A'):
            i += 1
            for j in range(len(l.curve_names)):
                l.curve_data.append([])
            if data_wrap == False:
                while i < len(lines):
                    temp = lines[i].split(' ')
                    values = []
                    for j in range(len(temp)):
                        if len(temp[j]) > 0:
                            try:
                                d = float(temp[j])
                                values.append(d)
                            except:
                                values.append(temp[j])
                    if len(values) > 0:
                        for j in range(len(values)):
                            l.curve_data[j].append(values[j])
                    i += 1
    return l

def append_curves(las, curve_names, curve_units, curve_desc, curve_data):
    return -1
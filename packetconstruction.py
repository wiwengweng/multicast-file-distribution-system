import struct
import uuid

from protocol_codes.packet_constants import PacketKeyEnum
from protocol_codes.message_code import MessageCodeEnum
from packet_construction_abstract import PacketStructFormats

class PacketConstructor(PacketStructFormats) :

	# assembles a packet to start initial file transmission
	def assemble_file_init_packet(self, filename, file_uuid, num_seqs):

		app_packet = struct.pack(self.init_packet_format, filename, file_uuid, num_seqs)

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.FILE_INIT, app_packet)

		return packet

	# assemble packet for file init response
	def assemble_file_resp_packet(self, file_uuid):

		app_packet = struct.pack(self.resp_packet_format, file_uuid)

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.FILE_INIT_RESP, app_packet)

		return packet

	# assemble packet for a piece of file data, given which sequence it is a part of
	# and also where in the sequence it lies
	def assemble_file_data_packet(self, file_uuid, seq_id, chunk_id, file_data) :

		app_packet = struct.pack(self.file_data_packet_format, file_uuid, seq_id, chunk_id, file_data)

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.FILE_DATA, app_packet)

		return packet

	# assemble a packet for checking whether or not the client received
	# all of the packets or not
	def assemble_seq_check_packet(self, file_uuid, seq_id) :

		app_packet = struct.pack(self.seq_check_packet_format, file_uuid, seq_id)

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.SEQ_CHECK, app_packet)

		return packet

	# assemble a packet to respond missing chunks call
	def assemble_missing_chunks_packet(self, file_uuid, seq_id, is_missing_chunks, missing_chunk_ids) :

		missing_chunks_part = ""
		if is_missing_chunks :

			missing_chunks_part = self.convert_missing_chunks_list(missing_chunk_ids)

		else :

			missing_chunks_part = ""

		app_packet = struct.pack(self.missing_chunks_packet_format, file_uuid, seq_id) + self.

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.MISSING_PACKETS_REQ, app_packet)

		return packet

	# assemble a packet for the end of transmission message
	def assemble_end_transmission_packet(self, file_uuid, last_seq, last_chunk) :

		app_packet = struct.pack(self.end_transmission_packet_format)

		packet = self.assemble_generic_packet_parts(MessageCodeEnum.END_OF_FILE_TRANSMISSION, packetdata)

		return packet

	# # assemble a packet for successful transmission
	# def assemble_successful_transmission_packet(self, file_uuid) :

	# def assemble_generic_struct(self, packettype, packetsegs) :

	# assembles the packet with the given packet type message and the packet segments
	def assemble_generic_packet_parts(self, packettype, app_packet) :

		return packet_to_send = struct.pack(self.general_header_format, PacketKeyEnum.PROTOCOL_NAME, packettype) + app_packet

	# takes a key and a value and assembles it in the packet format
	def assemble_packet_value(self, key, value) :
		return key + PacketKeyEnum.MAPPING_SEPARATOR + value + PacketKeyEnum.VALUE_SEPARATOR

	# convert the list of missing pacets into a string
	# of comma separated values of the packets
	# that are missing
	def convert_missing_chunks_list(missing_chunks_list) :

		return PacketKeyEnum.DATA_SEPARATOR.join(missing_chunks_list)

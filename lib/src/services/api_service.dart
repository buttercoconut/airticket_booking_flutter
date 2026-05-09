import 'dart:convert';
import 'package:http/http.dart' as http;
import '../models/flight.dart';

class ApiService {
  static const String _baseUrl = 'https://api.example.com';

  static Future<List<Flight>> searchFlights(String query) async {
    final url = Uri.parse('$_baseUrl/flights?search=$query');
    final response = await http.get(url);
    if (response.statusCode != 200) {
      throw Exception('Failed to load flights');
    }
    final List<dynamic> data = jsonDecode(response.body) as List<dynamic>;
    return data.map((e) => Flight.fromJson(e as Map<String, dynamic>)).toList();
  }
}
